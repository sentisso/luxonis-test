DROP TABLE IF EXISTS sreality_estates;
CREATE TABLE sreality_estates
(
    id        serial                                              NOT NULL PRIMARY KEY,
    hash_id   bigint                                              NOT NULL UNIQUE,
    title     character varying(255) COLLATE pg_catalog."default" NOT NULL,
    image_url character varying(255) COLLATE pg_catalog."default" NOT NULL
);