// React Components
// Table
var Table = React.createClass({
	render: function() {
		return (
      <table className="react-table">
				<TableHeader cols={this.props.cols} />
				<TableBody cols={this.props.cols} data={this.props.data}/>
			</table>
		);
	}
});

var TableHeader = React.createClass({
	render: function() {
			var columnHeaders = this.props.cols.map(function(col) {
			return(<th> {col.name} </th>);
		});
		return (
			<thead>
				<tr>{columnHeaders}</tr>
			</thead>
    );
	}
});

var TableBody = React.createClass({
	render: function() {
		var rows = this.props.data.map(function(row) {
			return(
				<TableRow rowData={row} cols={this.props.cols} />
			);
		}.bind(this));
		return (
			<tbody>
				{rows}
			</tbody>
		);
	}
});

var TableRow = React.createClass({
    render: function() {
        var row = this.props.cols.map(function(col) {
            var default_format = (val) => val;
            var format = col.format || default_format;
            var data = this.props.rowData[col.key]
            if (format == 'href') {
            return (
                <td>
                    <a href={data}>{data}</a>
                </td>
            );
            } else {
                return(
                    <td>
                        {format(data)}
                    </td>
                );
            }
        }.bind(this));
        return (
                <tr>
                {row}
            </tr>
        );
    }
});

// Form
var UrlForm = React.createClass({
    getInitialState: function() {
        return {url: '', title: '', description: ''};
    },
    handleUrlChange: function(e) {
        this.setState({url: e.target.value});
    },
    handleTitleChange: function(e) {
        this.setState({title: e.target.value});
    },
    handleDescChange: function(e) {
        this.setState({description: e.target.value});
    },
    handleSubmit: function(e) {
        e.preventDefault();
        var url = this.state.url.trim();
        var title = this.state.title.trim();
        var description = this.state.description.trim();
        if (!url) {
            return;
        }
        this.props.onUrlSubmit({url: url, title: title, description: description});
        this.setState({url: '', title: '', description: ''});
    },
    render: function() {
        return (
            <form className="urlForm" onSubmit={this.handleSubmit}>
                <h2>Get a new URL Shorty</h2>
                <input
                    type="text"
                    placeholder="A URL"
                    value={this.state.url}
                    onChange={this.handleUrlChange}
                /><br />
                <input
                    type="text"
                    placeholder="URL Title"
                    value={this.state.title}
                    onChange={this.handleTitleChange}
                /><br />
                <input
                    type="text"
                    placeholder="Your description"
                    value={this.state.description}
                    onChange={this.handleDescChange}
                /><br />
                <input type="submit" value="Post" />
            </form>
        );
    }
});

// Container & state management
var UrlContainer = React.createClass({
    loadUrlFromServer: function() {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    handleUrlSubmit: function(url_data) {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            type: 'POST',
            data: url_data,
            sucess: function(data) {
                this.setState({data: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    getInitialState: function() {
        return {data: []};
    },
    componentDidMount: function() {
        this.loadUrlFromServer();
        setInterval(this.loadUrlFromServer, this.props.pollInterval);
    },
    render: function() {
        return (
            <div className="urlContainer">
                <UrlForm onUrlSubmit={this.handleUrlSubmit}/>
                <Table
                    url={this.props.url}
                    pollInterval={this.props.pollInterval}
                    data={this.state.data}
                    cols={this.props.cols}
                />
            </div>
        );
    }
});

// constants for testing
// const API_URL = "http://localhost:8000/api/url/";

const VISIBLE_COLUMNS = [
    {key: 'url', name: 'URL Link', format: 'href'},
    {key: 'title', name: 'URL Title'},
    {key: 'description', name: 'URL Description'},
    {key: 'short_url', name: 'Shorty URL', format: 'href'}
];

const TEST_DATA = [
    {url: 'http://www.google.com/', title: 'Google', description: 'It\'s Google!', short_url: 'test'},
    {url: 'http://dvndrsn.com', title: 'Dave A.', description: 'It\'s me!', short_url: 'test'},
    {url: 'http://www.flocabulary.com', title: 'Flocabulary', description: 'Hi!', short_url: 'test'},
];

const POLL_INTERVAL = 5000;

// React Render
const render = () => {
	ReactDOM.render(
    <UrlContainer
      url= {API_URL}
      // data = {TEST_DATA}
      cols = {VISIBLE_COLUMNS}
      pollInterval = {POLL_INTERVAL}
    />,
		document.getElementById('content')
	);
};

render();
