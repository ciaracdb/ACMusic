let React = require('react');
let ReactDOM = require('react-dom');

class App extends React.Component {
    render() {
        return (
            <h1>
                Hello, React!
            </h1>
        )
    }
}

$.ajax({
    url: '/dbapi/playlists.json',
}).done(data => {
    console.log(data);
});

$.ajax({
    url: '/dbapi/playlists.json',
    method: 'POST',
    data: JSON.stringify({
        name: 'test',
        url: 'https://www.youtube.com/playlist?list=PLYgkQ-QH58rqIKAYL7AesKHz3wWqJ35gK'
    }),
    beforeSend: function(xhr) {
        xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
    },
    contentType: "application/json"
}).done(data => {
    console.log(data);
});

ReactDOM.render(<App/>, document.getElementById('container'));