'use strict';
/*
 * Complete the 'findFirstAvailableParkingSpot' function below.
 */

const dictionary = {
    regular: ['R'],
    small: ['R', 'S'],
    motorcycle: ['R', 'S', 'M'],
}

function findFirstAvailableParkingSpot(parkingSpots, vehicleType) {
    // Write your code here
    const possibilities = dictionary[vehicleType];
    let retVal = []
    
    for (var yCoordinate = 0; yCoordinate < parkingSpots.length; yCoordinate++) {
        const xArray = parkingSpots[yCoordinate]

        for (var xCoordinate = 0; xCoordinate < xArray.length; xCoordinate++) {
            const spot = xArray[xCoordinate];
            
            if (possibilities.includes(spot)) {
                retVal.push([xCoordinate, yCoordinate])
            }
        }
    }
    
    return retVal.length > 0 ? retVal : false
}
