define( "app/test",
    ['backbone'],
    function(){
        return {
            foo : function(str){
                console.log('module test, function foo '+'args = ', str);
                return 1;
            },
            bar: function(){
                console.log('Ubderscore test');
                console.log('_.map '+ _.map([1, 2, 3], function(num){ return num * 3; }));
                console.log('jQuery test');
                console.log('$.map '+ $.map([1, 2, 3], function(num){ return num * 3; }));
                return 1;
            }
        };
    }
);