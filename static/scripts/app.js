/**
 * Created by rizky on 11/22/15.
 */

This.Angular = angular.module('app',[])
.controller('mainController', ['$scope', '$http', function ($scope, $http) {
        $scope.number = 0;

        $scope.addNum = function() {
        var data = $.param({
            json: JSON.stringify({
                num: $scope.number
            })
        });
        $http.post("/addNum", data).success(function(data, status) {
            // do something if it's a success
            console.log("success!");
        })}
    }]);