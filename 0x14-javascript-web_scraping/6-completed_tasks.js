#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, resp, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const completedTask = {};
    todos.forEach((todo) => {
      if (todo.completed && completedTask[todo.userId] === undefined) {
        completedTask[todo.userId] = 1;
      } else if (todo.completed) {
        completedTask[todo.userId] += 1;
      }
    });
    console.log(completedTask);
  }
}
);
