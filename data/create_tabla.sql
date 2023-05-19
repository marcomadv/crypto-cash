CREATE TABLE "tabla" (
	"id"	INTEGER UNIQUE ,
	"date"	TEXT ,
	"time"	TEXT ,
	"moneda_from"	TEXT ,
	"cantidad_from"	REAL ,
	"moneda_to"	TEXT ,
	"cantidad_to"	REAL ,
	PRIMARY KEY("id" AUTOINCREMENT)
)