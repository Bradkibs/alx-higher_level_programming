#!/usr/bin/node
exports.addMeMaybe = function (number, theFunc) {
  theFunc(++number);
};
