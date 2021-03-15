const product = function() {
    console.log(arguments);
    return [].reduce.call(arguments, function(res, elem) {
        return res * elem;
    }, this.product);
};

const contextObj = {
    product: 10
};

const getProduct = product.bind(contextObj, 2, 3);
