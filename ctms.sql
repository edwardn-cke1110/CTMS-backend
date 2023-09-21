-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 11, 2023 at 12:23 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ctms`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `PatientID` int(6) NOT NULL,
  `FirstName` text NOT NULL,
  `LastName` text NOT NULL,
  `DateOfBirth` date NOT NULL,
  `Address` varchar(255) NOT NULL,
  `ContactNumber` text NOT NULL,
  `StudyID` int(6) NOT NULL,
  `TreatmentID` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`PatientID`, `FirstName`, `LastName`, `DateOfBirth`, `Address`, `ContactNumber`, `StudyID`, `TreatmentID`) VALUES
(1, 'Johnson', 'Jack', '1991-09-18', '155 Sydney St, Sydney, NSW 2000', '046839471', 1, 1),
(2, 'Mary', 'Johnson', '2002-09-04', '96 Old Street, Sydney, NSW 2008', '0469832145', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `privilege group`
--

CREATE TABLE `privilege group` (
  `PrivilegeID` int(1) NOT NULL,
  `GroupName` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `privilege group`
--

INSERT INTO `privilege group` (`PrivilegeID`, `GroupName`) VALUES
(1, 'Doctor'),
(2, 'Nurse'),
(3, 'Admin');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `StaffID` int(6) NOT NULL,
  `FirstName` text NOT NULL,
  `LastName` text NOT NULL,
  `DateOfBirth` date NOT NULL,
  `ContactNumber` text NOT NULL,
  `PrivilegeID` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`StaffID`, `FirstName`, `LastName`, `DateOfBirth`, `ContactNumber`, `PrivilegeID`) VALUES
(1, 'Jack', 'Pierce', '1995-09-03', '0494758691', 1),
(2, 'Mark', 'Peter', '1997-09-26', '0436521896', 3);

-- --------------------------------------------------------

--
-- Table structure for table `staffstudy`
--

CREATE TABLE `staffstudy` (
  `StaffID` int(6) NOT NULL,
  `StudyID` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffstudy`
--

INSERT INTO `staffstudy` (`StaffID`, `StudyID`) VALUES
(1, 1),
(2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `study`
--

CREATE TABLE `study` (
  `StudyID` int(6) NOT NULL,
  `StudyName` text NOT NULL,
  `Observations` mediumtext NOT NULL,
  `Status` text NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `Duration` varchar(255) NOT NULL,
  `TreatmentID` int(6) NOT NULL,
  `OrganisationID` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `study`
--

INSERT INTO `study` (`StudyID`, `StudyName`, `Observations`, `Status`, `StartDate`, `EndDate`, `Duration`, `TreatmentID`, `OrganisationID`) VALUES
(1, 'Eradicate Cancer', 'Patient just started taking doses', 'On-going', '2023-09-06', '2023-09-22', '16 days', 1, 1),
(2, 'Dementia', 'Patients can\'t remember things', 'On-going', '2023-07-04', '2023-10-18', '3 months', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `treatment`
--

CREATE TABLE `treatment` (
  `TreatmentID` int(6) NOT NULL,
  `TreatmentName` text NOT NULL,
  `Supplier` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `treatment`
--

INSERT INTO `treatment` (`TreatmentID`, `TreatmentName`, `Supplier`) VALUES
(1, 'Cancer-Free', 'Cancer Council of NSW'),
(2, 'Alzheimers', 'Mega Pharma Pty Ltd');

-- --------------------------------------------------------

--
-- Table structure for table `trial organisation`
--

CREATE TABLE `trial organisation` (
  `OrganisationID` int(6) NOT NULL,
  `OrganisationName` text NOT NULL,
  `ContactNumber` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trial organisation`
--

INSERT INTO `trial organisation` (`OrganisationID`, `OrganisationName`, `ContactNumber`) VALUES
(1, 'Future Research Pty Ltd', '0468394713'),
(2, 'PharmaCompany', '0295632847');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`PatientID`),
  ADD KEY `TreatmentID` (`TreatmentID`),
  ADD KEY `StudyID` (`StudyID`);

--
-- Indexes for table `privilege group`
--
ALTER TABLE `privilege group`
  ADD PRIMARY KEY (`PrivilegeID`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`StaffID`),
  ADD KEY `PrivilegeID` (`PrivilegeID`);

--
-- Indexes for table `staffstudy`
--
ALTER TABLE `staffstudy`
  ADD PRIMARY KEY (`StaffID`,`StudyID`),
  ADD KEY `StudyID` (`StudyID`);

--
-- Indexes for table `study`
--
ALTER TABLE `study`
  ADD PRIMARY KEY (`StudyID`),
  ADD KEY `TreatmentID` (`TreatmentID`),
  ADD KEY `OrganisationID` (`OrganisationID`);

--
-- Indexes for table `treatment`
--
ALTER TABLE `treatment`
  ADD PRIMARY KEY (`TreatmentID`);

--
-- Indexes for table `trial organisation`
--
ALTER TABLE `trial organisation`
  ADD PRIMARY KEY (`OrganisationID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `patient`
--
ALTER TABLE `patient`
  ADD CONSTRAINT `patient_ibfk_2` FOREIGN KEY (`TreatmentID`) REFERENCES `treatment` (`TreatmentID`),
  ADD CONSTRAINT `patient_ibfk_3` FOREIGN KEY (`StudyID`) REFERENCES `study` (`StudyID`);

--
-- Constraints for table `staff`
--
ALTER TABLE `staff`
  ADD CONSTRAINT `staff_ibfk_2` FOREIGN KEY (`PrivilegeID`) REFERENCES `privilege group` (`PrivilegeID`);

--
-- Constraints for table `staffstudy`
--
ALTER TABLE `staffstudy`
  ADD CONSTRAINT `staffstudy_ibfk_1` FOREIGN KEY (`StaffID`) REFERENCES `staff` (`StaffID`),
  ADD CONSTRAINT `staffstudy_ibfk_2` FOREIGN KEY (`StudyID`) REFERENCES `study` (`StudyID`);

--
-- Constraints for table `study`
--
ALTER TABLE `study`
  ADD CONSTRAINT `study_ibfk_1` FOREIGN KEY (`TreatmentID`) REFERENCES `treatment` (`TreatmentID`),
  ADD CONSTRAINT `study_ibfk_4` FOREIGN KEY (`OrganisationID`) REFERENCES `trial organisation` (`OrganisationID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
