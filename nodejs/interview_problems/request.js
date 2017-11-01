var request = require('request');

var callback = function (error, response, body) {
    if (!error && response.statusCode == 200) {
          //console.log(body) // Show the HTML for the Google homepage. 

        }
}

request('http://www.google.com', callback )


/*accountant("my sales/expense", function (tax_return_information) {*/

  //var taxReturnAmount = tax_return_information.taxReturnAmount
  //if (taxReturnAmount < 400) {
    //"let's have a meeting. I'm angry."
  //} else if (taxReturnAmount > 1000) {
    //"call me anyway and let's get a beer"
  //}
/*}*/
