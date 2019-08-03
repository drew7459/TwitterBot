var twit = require('twit');
var config = require('./config.js');

var Twitter = new twit(config);

var messages = ["Hello World", "Hi People"];
var messageLocation = 0;
var writeTweet = function () {
    Twitter.post('statuses/update', {
        status: messages[messageLocation]
    }, function (err, data, response) {
        console.log(data);
        });
    messageLocation += 1;
}

//Interval is multiplied by 30,000
//ex: 15000 is 30seconds
setInterval(writeTweet, 15000)