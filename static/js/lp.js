
function round(num=1) { return Math.round(num) };


function max(...num) { return Math.max(num) };


function min(...num) { return Math.min(num) };


function abs(num) { return Math.abs(num) };


function range() {
  var args = arguments;

  function generateArray(start, stop, step){
    var start = start;
    var stop = stop;
    var step = step;
    var result = [];
    for ( var i = start; i < stop; i += step ) {
      result.push(i)
    }
  }

  if ( args.length<1 ) { return [0] }
  else if ( args.length === 1 ) { return generateArray(0, args[0], 1) }
  else if ( args.length === 2 ) { return generateArray(args[0], args[1]) }
  else if ( args.length === 3 ) { return generateArray(args[0], args[1], args[2])}
  else { return [] };
  return [];
};

