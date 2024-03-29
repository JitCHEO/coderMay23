const express = require('express');
const router = express.Router();
const { Pet } = require('../models/PetModel');

// Find all pets in the DB
router.get("/all", async (request, response) => {
    let result = await Pet.find();

    response.json({
        pets: result
    });
})

// Finds one pet by its id
router.get("/:id", async(request, response) => {
    let result = null;

    response.json({
        pet: result
    });
})

// Find one pet by its name
router.get("/search/name/:name", async(request, response) => {
    let result = null;

    response.json({
        pet: result
    });
})

// find all the pets of the same type
router.get("/search/type/:type", async(request, response) => {
    let result = null;

    response.json({
        pet: result
    });
})

//Create a new pet in the DB
//POST localhost:3000/pets/
router.post("/", async(request, response)=>{
    let result = await Pet.create(request.body);

    response.json({
        pet: result
    })
})


module.exports = router;