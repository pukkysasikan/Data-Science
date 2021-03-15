-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 15, 2021 at 03:11 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `opencvfrom`
--

-- --------------------------------------------------------

--
-- Table structure for table `testfrom`
--

CREATE TABLE `testfrom` (
  `id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(255) NOT NULL,
  `path_img` varchar(255) NOT NULL,
  `date_upload` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `testfrom`
--

INSERT INTO `testfrom` (`id`, `fname`, `lname`, `phone`, `email`, `path_img`, `date_upload`) VALUES
(1, 'ศศิกานต์', 'อินวิถี', '0613890852', 'pukkysasikan@gmail.com', './static/uploads/cds23373952-1.jpg', '2021-03-15 20:55:36.871852'),
(2, 'จตุพร', 'ทองเกษม', '0628269908', 'pukkysasikan@gmail.com', './static/uploads/Screenshot_2021-01-07_112700.png', '2021-03-15 20:58:00.147156'),
(3, 'จตุพร', 'ทองเกษม', '0628269908', 'pukkysasikan@gmail.com', './static/uploads/Screenshot_2021-01-07_112700.png', '2021-03-15 20:58:11.986340'),
(4, 'จตุพร', 'ทองเกษม', '0613890852', 'sasikan.in.62@ubu.ac.th', './static/uploads/cds23373952-1.jpg', '2021-03-15 20:58:30.752506');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `testfrom`
--
ALTER TABLE `testfrom`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `testfrom`
--
ALTER TABLE `testfrom`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
