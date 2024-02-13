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


-- --------------------------------------------------------

--
-- Struttura della tabella `squadra`
--

CREATE TABLE `squadra` (
  `id_squadra` int(11) PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `squadra`
--


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
--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `risultati`
--


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
