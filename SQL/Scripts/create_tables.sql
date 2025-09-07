CREATE DATABASE InventarioDB;

GO

USE InventarioDB;

GO

-- Tabla PurchasePrices

CREATE TABLE PurchasePrices (
	Brand			VARCHAR(100),
	Description		VARCHAR(255),
	Price			DECIMAL(10,2),
	Size			VARCHAR(50),
	Volume			VARCHAR(50),
	Classification	VARCHAR(100),
	PurchasePrice	DECIMAL(10,2),
	VendorNumber	INT,
	VendorName		VARCHAR(100)
);

-- Tabla BegInv

CREATE TABLE BegInv (
	InventoryId     INT PRIMARY KEY,
    Store           VARCHAR(100),
    City            VARCHAR(100),
    Brand           VARCHAR(100),
    Description     VARCHAR(255),
    Size            VARCHAR(50),
    onHand          INT,
    Price           DECIMAL(10,2),
    startDate       DATE
);

-- 3. Tabla: EndInv
CREATE TABLE EndInv (
    InventoryId     INT,
    Store           VARCHAR(100),
    City            VARCHAR(100),
    Brand           VARCHAR(100),
    Description     VARCHAR(255),
    Size            VARCHAR(50),
    onHand          INT,
    Price           DECIMAL(10,2),
    endDate         DATE
);

-- 4. Tabla: InvoicePurchases
CREATE TABLE InvoicePurchases (
    VendorNumber    INT,
    VendorName      VARCHAR(100),
    InvoiceDate     DATE,
    PONumber        VARCHAR(50),
    PODate          DATE,
    PayDate         DATE,
    Quantity        INT,
    Dollars         DECIMAL(12,2),
    Freight         DECIMAL(12,2),
    Approval        VARCHAR(50)
);

-- 5. Tabla: Purchases
CREATE TABLE Purchases (
    InventoryId     INT,
    Store           VARCHAR(100),
    Brand           VARCHAR(100),
    Description     VARCHAR(255),
    Size            VARCHAR(50),
    VendorNumber    INT,
    VendorName      VARCHAR(100),
    PONumber        VARCHAR(50),
    PODate          DATE,
    ReceivingDate   DATE,
    InvoiceDate     DATE,
    PayDate         DATE,
    PurchasePrice   DECIMAL(10,2),
    Quantity        INT,
    Dollars         DECIMAL(12,2),
    Classification  VARCHAR(100)
);

-- 6. Tabla: Sales
CREATE TABLE Sales (
    InventoryId     INT,
    Store           VARCHAR(100),
    Brand           VARCHAR(100),
    Description     VARCHAR(255),
    Size            VARCHAR(50),
    SalesQuantity   INT,
    SalesDollars    DECIMAL(12,2),
    SalesPrice      DECIMAL(10,2),
    SalesDate       DATE,
    Volume          VARCHAR(50),
    Classification  VARCHAR(100),
    ExciseTax       DECIMAL(12,2),
    VendorNo        INT,
    VendorName      VARCHAR(100)
);