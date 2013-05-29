define("app/last",
    ['backbone', 'app/hest'],
    function(Backbone, hest){
        return {
            ad: function(){
                hest.one();
                return 1;
            }
        }
    }
);
