/* Symmetric difference is a binary operation, 
which means it operates on only two elements. So to evaluate an expression 
involving symmetric differences among three elements (A △ B △ C),
 you must complete one operation at a time. Thus, for sets A and B above, 
and C = {2, 3}, A △ B △ C = (A △ B) △ C = {1, 4} △ {2, 3} = {1, 2, 3, 4}.

Create a function that takes two or more arrays and returns 
an array of their symmetric difference. The returned array must 
contain only unique values (no duplicates). */

// função simetria
function sym() {

    // variable arg with a empty array
    var args = [];

    //condional pra puxar index
    for (var i = 0; i < arguments.length; i++) {

        // metodo push
      args.push(arguments[i]);
    }
  
    //função diferença entre as dias arrays
    function symDiff(arrayOne, arrayTwo) {
        // variavel que tem uma array vazia que vai receber o resultado da pesquisa
      var result = [];
  
      // metodo for.each faz a mesma funçao com todos os itens da lista
      arrayOne.forEach(function(item) {

        // condicional se a array 2 é maior que 0, e o resultado do index of ee maior que 0, adiciona ele na lista 
        if (arrayTwo.indexOf(item) < 0 && result.indexOf(item) < 0) {
          result.push(item);
        }
      });


   arrayTwo.forEach(function(item) {
        if (arrayOne.indexOf(item) < 0 && result.indexOf(item) < 0) {
          result.push(item);
        }
      });
  
      return result;
    }
    return args.reduce(symDiff);
}

  
    // Apply reduce method to args array, using the symDiff function
  
  
  //running test
  console.log(sym([1, 2, 3], [5, 2, 1, 4]));
  console.log(sym([1, 2, 3, 3], [5, 2, 1, 4]));
  console.log(sym([1, 2, 5], [2, 3, 5], [3, 4, 5]));
  console.log(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]));
  
