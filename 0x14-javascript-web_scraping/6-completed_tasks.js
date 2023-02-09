#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, resp, body) => {
	if (!error) {
		const todos = JSON.parse(body);
		const completed_task = {};
		todos.forEach((todo) => {
			if (todo.completed && completed_task[todo.userId] === undefined) {
				completed_task[todo.userId] = 1;
			} else if (todo.completed) {
				completed_task[todo.userId] += 1;
			}
		});
		console.log(completed_task);
	}
}
);

