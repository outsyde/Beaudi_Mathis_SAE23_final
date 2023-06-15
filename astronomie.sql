SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de données : `astronomie`
--

-- --------------------------------------------------------

--
-- Structure de la table `materiel`
--

DROP TABLE IF EXISTS `materiel`;
CREATE TABLE IF NOT EXISTS `materiel` (
  `id_material` int NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  `prix` int NOT NULL,
  PRIMARY KEY (`id_material`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `objet`
--

DROP TABLE IF EXISTS `objet`;
CREATE TABLE IF NOT EXISTS `objet` (
  `id_objet` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(10) NOT NULL,
  `type` varchar(10) NOT NULL,
  `distanceTerre` int NOT NULL,
  `distanceSoleil` int NOT NULL,
  `distanceGalaxie` int DEFAULT NULL,
  `luminosite` int NOT NULL,
  `vitesse` int DEFAULT NULL,
  `age` int NOT NULL,
  PRIMARY KEY (`id_objet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `observe`
--

DROP TABLE IF EXISTS `observe`;
CREATE TABLE IF NOT EXISTS `observe` (
  `id_observe` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `lieu` varchar(10) NOT NULL,
  `observatoire/musée` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `filmObjet` varchar(10) DEFAULT NULL,
  `type` enum('soirée','journée') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `materiel` int NOT NULL,
  `objetObserve` int NOT NULL,
  PRIMARY KEY (`id_observe`),
  KEY `materiel` (`materiel`),
  KEY `objetObserve` (`objetObserve`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `proposition`
--

DROP TABLE IF EXISTS `proposition`;
CREATE TABLE IF NOT EXISTS `proposition` (
  `id_proposition` int NOT NULL AUTO_INCREMENT,
  `prenom` varchar(20) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `lieu` varchar(20) NOT NULL,
  `heure` int NOT NULL,
  `materiel` int NOT NULL,
  `objetObservable` int NOT NULL,
  PRIMARY KEY (`id_proposition`),
  KEY `materiel` (`materiel`),
  KEY `objetObservable` (`objetObservable`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Contraintes pour la table `observe`
--

ALTER TABLE `observe`
  ADD CONSTRAINT `meteriel_ibfk1` FOREIGN KEY (`materiel`) REFERENCES `materiel` (`id_material`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `objetObserve_ibfk4` FOREIGN KEY (`objetObserve`) REFERENCES `objet` (`id_objet`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Contraintes pour la table `proposition`
--

ALTER TABLE `proposition`
  ADD CONSTRAINT `meteriel_ibfk2` FOREIGN KEY (`materiel`) REFERENCES `materiel` (`id_material`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `objetObservable_ibfk3` FOREIGN KEY (`objetObservable`) REFERENCES `objet` (`id_objet`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;
