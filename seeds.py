from models.yarn import Yarn
from models.colour import Colour
from models.manufacturer import Manufacturer
from datetime import datetime as dt

from repositories import manufacturer_repository, yarn_repository, colour_repository

manufacturer_repository.delete_all()
yarn_repository.delete_all()
colour_repository.delete_all()

####----- MANUFACTURERS -----####

caron = Manufacturer("Caron", dt(2023, 1, 5), 35000)
cascade = Manufacturer("Cascade", dt(2022, 12, 15), 0)
sirdar = Manufacturer("Sirdar", dt(2022, 6, 28), 57800)
manufacturer_repository.save(caron)
manufacturer_repository.save(cascade)
manufacturer_repository.save(sirdar)


####----- YARNS -----####

sirdar_yarn1 = Yarn(
    "Hayfield",
    sirdar,
    "Super Chunky",
    100,
    72,
    10,
    "20% wool",
    250,
    350,
    "sirdar_hayfield_sc.jpeg",
)
caron_yarn1 = Yarn(
    "Cotton Angel Cakes",
    caron,
    "Aran",
    250,
    485,
    4.5,
    "60% cotton, 40% acrylic",
    900,
    1299,
    "caron_cotton_angel_cakes.jpeg",
)
cascade_yarn1 = Yarn(
    "Heritage",
    cascade,
    "4ply",
    100,
    400,
    3.25,
    "75% wool, 25% nylon",
    760,
    899,
    "cascade_heritage.jpeg",
)
cascade_yarn2 = Yarn(
    "Cantata",
    cascade,
    "Aran",
    100,
    200,
    5.5,
    "70% cotton, 30% wool",
    720,
    899,
    "cascade_cantata.jpeg",
)
cascade_yarn3 = Yarn(
    "Superwash",
    cascade,
    "DK",
    100,
    200,
    4.5,
    "100% wool",
    850,
    899,
    "cascade_superwash.jpeg",
)
yarn_repository.save(sirdar_yarn1)
yarn_repository.save(caron_yarn1)
yarn_repository.save(cascade_yarn1)
yarn_repository.save(cascade_yarn2)
yarn_repository.save(cascade_yarn3)


####----- COLOURS -----####

sirdar_hayfield_colour1 = Colour("Cornish", "#EBE4CE", 18, sirdar_yarn1)
sirdar_hayfield_colour2 = Colour("Oats", "#BD9C88", 3, sirdar_yarn1)
sirdar_hayfield_colour3 = Colour("Forget Me Not", "#7691CC", 6, sirdar_yarn1)
caron_cakes_colour1 = Colour("Faded Jeans", "#b3c1ca", 10, caron_yarn1)
caron_cakes_colour2 = Colour("Sunny Day", "#fad193", 14, caron_yarn1)
cascade_heritage_colour1 = Colour("Raspberry", "#c22a72", 22, cascade_yarn1)
cascade_heritage_colour2 = Colour("Royal", "#2863aa", 0, cascade_yarn1)
cascade_heritage_colour3 = Colour("Primavera", "#8cad52", 35, cascade_yarn1)
cascade_heritage_colour4 = Colour("Real Black", "#111111", 27, cascade_yarn1)
cascade_heritage_colour5 = Colour("Deep Ocean", "#28515e", 7, cascade_yarn1)
cascade_cantata_colour1 = Colour("Turquoise", "#52c4df", 30, cascade_yarn2)
cascade_cantata_colour2 = Colour("Plum", "#5c1d5d", 0, cascade_yarn2)
cascade_cantata_colour3 = Colour("Icy Grey", "#acb1bc", 5, cascade_yarn2)
cascade_cantata_colour4 = Colour("Clay", "#5e4d48", 28, cascade_yarn2)
cascade_superwash_colour1 = Colour("Turtle", "#7c7a47", 15, cascade_yarn3)
cascade_superwash_colour2 = Colour("Desert Sun", "#e37e28", 25, cascade_yarn3)
cascade_superwash_colour3 = Colour("Seafoam Heather", "98d1da", 32, cascade_yarn3)

colour_repository.save(sirdar_hayfield_colour1)
colour_repository.save(sirdar_hayfield_colour2)
colour_repository.save(sirdar_hayfield_colour3)
colour_repository.save(caron_cakes_colour1)
colour_repository.save(caron_cakes_colour2)
colour_repository.save(cascade_heritage_colour1)
colour_repository.save(cascade_heritage_colour2)
colour_repository.save(cascade_heritage_colour3)
colour_repository.save(cascade_heritage_colour4)
colour_repository.save(cascade_heritage_colour5)
colour_repository.save(cascade_cantata_colour1)
colour_repository.save(cascade_cantata_colour2)
colour_repository.save(cascade_cantata_colour3)
colour_repository.save(cascade_cantata_colour4)
colour_repository.save(cascade_superwash_colour1)
colour_repository.save(cascade_superwash_colour2)
colour_repository.save(cascade_superwash_colour3)
