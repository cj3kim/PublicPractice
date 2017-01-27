var _ = require("underscore");

function make_change (change, denominations ) {
  var answer = 0;
  for (var i = 0, l = denominations.length; i < l; i++) {
    var denomination = denominations[i];
    var remainder = change - denomination;

    if (remainder < 0) {
      break
    }

    if (remainder === 0) {
      return 1;
    } else {
      answer += make_change(remainder, denominations)
    }
  }
  return answer;

}



module.exports = make_change
