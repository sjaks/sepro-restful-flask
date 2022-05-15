CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE secrets(
    "id" uuid DEFAULT uuid_generate_v4 (),
    "value" TEXT,
    PRIMARY KEY (id)
);
