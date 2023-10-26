sql
CREATE TABLE IF NOT EXIST scooter (
    scooter_id      SMALLINT NOT NULL
    ,FLAG           ENUM('online', 'offline', 'lost/stolen') NOT NULL DEFAULT 'offline'
    ,PRIMARY KEY (scooter_id)
)

CREATE TABLE IF NOT EXIST customer (
    user_id                 MEDIUMINT NOT NULL
    ,credit_card_number     CHAR(16) NOT NULL
    ,expiration_date        VARCHAR(10)
    ,user_email             VARCHAR(100) NOT NULL
    ,PRIMARY KEY (user_id)
)

CREATE TABLE IF NOT EXIST trip (
    trip_id                 MEDIUMINT NOT NULL
    ,user_id                CHAR(16) NOT NULL
    ,scooter_id             VARCHAR(10)
    ,start_time             NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,end_time               TIMESTAMP
    ,pickup_latitude        VARCHAR(20) NOT NULL
    ,pickup_longitude       VARCHAR(20) NOT NULL
    ,dropoff_latitude       VARCHAR(20)
    ,dropoff_longitude      VARCHAR(20)
    ,PRIMARY KEY (trip_id)
    ,FOREIGN KEY (user_id) REFERENCES customer(user_id)
    ,FOREIGN KEY (scooter_id) REFERENCES scooter(scooter_id)
)