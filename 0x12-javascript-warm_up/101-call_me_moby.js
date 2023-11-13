#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let k = 0; k < x; k++) {
    theFunction();
  }
};
