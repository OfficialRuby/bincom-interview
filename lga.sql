DROP TABLE IF EXISTS lga;
CREATE TABLE IF NOT EXISTS lga (
  uniqueid SERIAL NOT NULL ,
  lga_id INT NOT NULL,
  lga_name varchar(50) NOT NULL,
  state_id INT NOT NULL,
  lga_description text,
  entered_by_user varchar(50) NOT NULL,
  date_entered varchar(50) ,
  user_ip_address varchar(50) NOT NULL,
  PRIMARY KEY (uniqueid)
) ;

--
-- Dumping data for table lga
--

INSERT INTO lga (uniqueid, lga_id, lga_name, state_id, lga_description, entered_by_user, date_entered, user_ip_address) VALUES
(1, 1, 'Aniocha North', 25, 'Aniocha North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.2'),
(2, 2, 'Aniocha - South', 25, 'Aniocha - South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(3, 5, 'Ethiope East', 25, 'Ethiope East', 'Bincom', '0000-00-00 00:00:00', '127.0.0.5'),
(4, 6, 'Ethiope West', 25, 'Ethiope West', 'Bincom', '0000-00-00 00:00:00', '127.0.0.6'),
(5, 7, 'Ika North - East', 25, 'Ika North - East', 'Bincom', '0000-00-00 00:00:00', '127.0.0.8'),
(6, 8, 'Ika - South', 25, 'Ika - South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.7'),
(7, 9, 'Isoko North', 25, 'Isoko North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.9'),
(8, 10, 'Isoko South', 25, 'Isoko South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.10'),
(9, 11, 'Ndokwa East', 25, 'Ndokwa East', 'Bincom', '0000-00-00 00:00:00', '127.0.0.11'),
(10, 12, 'Ndokwa West', 25, 'Ndokwa West', 'Bincom', '0000-00-00 00:00:00', '127.0.0.12'),
(11, 13, 'Okpe', 25, 'Okpe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.13'),
(12, 14, 'Oshimili - North', 25, 'Oshimili - North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.14'),
(13, 15, 'Oshimili - South', 25, 'Oshimili - South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.15'),
(14, 16, 'Patani', 25, 'Patani', 'Bincom', '0000-00-00 00:00:00', '127.0.0.16'),
(15, 17, 'Sapele', 25, 'Sapele', 'Bincom', '0000-00-00 00:00:00', '127.0.0.17'),
(16, 18, 'Udu', 25, 'Udu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.18'),
(17, 19, 'Ughelli North', 25, 'Ughelli North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.19'),
(18, 20, 'Ughelli South', 25, 'Ughelli South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.20'),
(19, 21, 'Ukwuani', 25, 'Ukwuani', 'Bincom', '0000-00-00 00:00:00', '127.0.0.21'),
(20, 22, 'Uvwie', 25, 'Uvwie', 'Bincom', '0000-00-00 00:00:00', '127.0.0.22'),
(21, 31, 'Bomadi', 25, 'Bomadi', 'Bincom', '0000-00-00 00:00:00', '127.0.0.3'),
(22, 32, 'Burutu', 25, 'Burutu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.4'),
(23, 33, 'Warri North', 25, 'Warri North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.23'),
(24, 34, 'Warri South', 25, 'Warri South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.24'),
(25, 35, 'Warri South West', 25, 'Warri South West', 'Bincom', '0000-00-00 00:00:00', '127.0.0.25');
