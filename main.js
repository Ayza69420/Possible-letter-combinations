function alg(n) {
    var x = [];
    var output = [];

    for (let i=0; i < n.length; i++) {
        x.push(n[i]);
    }

    for (let j=0; j<n.length; j++) {
        for (let i=1; i<n.length; i++) {
            xi = x[i];

            x[i] = x[i-1];
            x[i-1] = xi;

            output.push(x.join());
        }
    }

    return output
}

console.log(alg('test')); // Pass the word as the argument and it's gonna return all the possible combinations of the word's letters.
