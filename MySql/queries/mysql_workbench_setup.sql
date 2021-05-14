USE twitter;
SELECT * FROM tweets;
INSERT INTO tweets (tweet, user_id, created_at, updated_at)
VALUES ("Whoo, that was a fun clinic!",3,NOW(),NOW());
UPDATE tweets SET
tweet = "Whoo, that was a fun basketball clinic!"
WHERE id = 13;
DELETE FROM tweets
WHERE id > 13;