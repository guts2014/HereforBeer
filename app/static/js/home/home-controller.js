var module = angular.module('terrorismapp');

module.controller('HomeController', ['$scope', '$http', function ($scope, $http) {

    $scope.searchText = '';

    $scope.results = [];
    $scope.search = function() {

        //todo: remove this
        console.log('making request based to api based on search string' + $scope.searchText);

        $http({
            url: '/api/events',  // todo: check that this url is correct when api is made
            method: 'GET',
            params: {
                'description': '%' + $scope.searchText + '%' // todo: need to pass in correct field name if it changes
            }
        }).success(function(response) {
            $scope.results = response;
            console.log('callback success - in the api, all is good');
        }).error(function() {
            console.log('something went wrong, oh noes')
        });


    }

}]);
