define( "app/hest", ['jquery'],
    function($){
        return {
            one : function(){
                console.log('hest:one called');
                return 1;
            }
        };
    }
);