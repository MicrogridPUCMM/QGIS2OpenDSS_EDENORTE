# **QGIS2OpenDSS\_EDENORTE**

## Introduction - From GIS Layers to Power Simulation

To assess and study the impact of Distributed Generation (DG), and the design of Microgrid Architecture in the Medium Voltage (MV) and Low Voltage (LV) networks, it is necessary to have advanced simulation tools and detailed models of the Distribution Network and its components. In order to make these simulations more accessible, open-source software tools such as OpenDSS (Open Distribution System Simulator) are now frequently used by Utilities and Research Laboratories across the globe.

![image](https://github.com/MicrogridPUCMM/QGIS2OpenDSS_EDENORTE/assets/112496588/9b548bc8-fb36-4cba-9586-4bb858ca51b3)

However, simulation results with these tools highly depend on the quality and availability of network data (type, material, size and length of conductors, location and capacity of distribution transformers and capacitors) which is typically stored in the Geographical Information Systems (GIS) of power utilities. The necessary work to translate the GIS information to the respective power flow simulation tools is not only arduous but requires third party software packages to translate the data. In addition, any change in the database requires new iteration of data files exchanges among pieces of software which is proven to be tedious work when dealing with many distribution network feeders.

This repository presents the implementation of QGIS2OPENDSS, a plugin designed to automatically generate distribution network models for OpenDSS, which data comes directly from an open-source Geographic Information System (GIS) software environment, QGIS. This plugin was developed by researchers at the [EPER Lab](https://github.com/EPERLab/QGIS2OpenDSS) in the University of Costa Rica (UCR), and it's part of a series of tools under development to help researchers and power engineers to assess the evolution of distributed generation and power systems, reducing the time from model to simulation by orders of magnitude (months to weeks)

A working group has been created between PUCMM Researchers and EDENORTE´s Distribution, Planning and Network Study Department. The main objective of the group is to develop the processes and models to clean, fix, aggregate or remove incorrect, corrupted, incorrectly formatted, duplicated, or incomplete data within the GIS network dataset, in order to enable the data to be processed by the QGIS2OPENDSS plugin in QGIS.

## Repository content

**QGIS version: QGIS 3.18.3**

QGIS2OpenDSS version: [Modified by PUCMM Team](https://drive.google.com/drive/folders/1-5cYZdKdgDeJs1S0SwUIKKDuGMBl-Vnj?usp=sharing)

**Content:**

**There are 3 folders:**

1. **DSS** - Contains a sample of available residential, commercial, and industrial load profiles.

![image](https://github.com/MicrogridPUCMM/QGIS2OpenDSS_EDENORTE/assets/112496588/caee316e-b329-4c8d-9a4b-d30c56052794)


Fig 1 - Load profiles

1. **GIS** - Contains the GIS Layers:

![image](https://github.com/MicrogridPUCMM/QGIS2OpenDSS_EDENORTE/assets/112496588/9c59ae58-8a35-4b47-9e59-10ba3fa22164)


Fig 2 - Basic GIS layers required by the plugin.

1. Test – Contains the output files of the QGIS2OpenDSS for the modelled circuit. VOLG101.

![image](https://github.com/MicrogridPUCMM/QGIS2OpenDSS_EDENORTE/assets/112496588/515c995d-fcf4-45fa-ab76-77dc2723da4f)


Fig 3 - QGIS2OpenDSS file creator output

**Limitations - Update (02-09-2022)**

- There is no commercial nor industrial loads in these model
- Data Dictionaries and Guidelines need to be updated to reflect lastest changes

