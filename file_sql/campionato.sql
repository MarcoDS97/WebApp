-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Feb 09, 2024 alle 10:30
-- Versione del server: 10.4.32-MariaDB
-- Versione PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `campionato`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `risultati`
--

CREATE TABLE `risultati` (
  `id_risultato` int(11) NOT NULL,
  `gs1` int(11) NOT NULL,
  `gs2` int(11) NOT NULL,
  `giornata` int(11) NOT NULL,
  `id_s1` int(11) NOT NULL,
  `id_s2` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `risultati`
--

INSERT INTO `risultati` (`id_risultato`, `gs1`, `gs2`, `giornata`, `id_s1`, `id_s2`) VALUES
(1, 3, 2, 1, 2, 3),
(2, 2, 2, 1, 1, 4),
(3, 0, 1, 2, 2, 1),
(4, 2, 2, 2, 3, 4),
(5, 3, 1, 3, 2, 4),
(6, 2, 2, 3, 3, 1);

-- --------------------------------------------------------

--
-- Struttura della tabella `squadra`
--

CREATE TABLE `squadra` (
  `id_squadra` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `squadra`
--

INSERT INTO `squadra` (`id_squadra`, `nome`) VALUES
(1, 'Milan'),
(2, 'Inter'),
(3, 'Juventus'),
(4, 'Roma');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `risultati`
--
ALTER TABLE `risultati`
  ADD PRIMARY KEY (`id_risultato`),
  ADD KEY `fk_s1` (`id_s1`),
  ADD KEY `fk_s2` (`id_s2`);

--
-- Indici per le tabelle `squadra`
--
ALTER TABLE `squadra`
  ADD PRIMARY KEY (`id_squadra`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `risultati`
--
ALTER TABLE `risultati`
  MODIFY `id_risultato` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT per la tabella `squadra`
--
ALTER TABLE `squadra`
  MODIFY `id_squadra` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `risultati`
--
ALTER TABLE `risultati`
  ADD CONSTRAINT `fk_s1` FOREIGN KEY (`id_s1`) REFERENCES `squadra` (`id_squadra`),
  ADD CONSTRAINT `fk_s2` FOREIGN KEY (`id_s2`) REFERENCES `squadra` (`id_squadra`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
