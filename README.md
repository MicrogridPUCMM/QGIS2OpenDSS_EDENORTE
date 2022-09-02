# QGIS2OpenDSS_EDENORTE

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><strong>Introduction</strong> - From GIS Layers to Power Simulation</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"justify","style":{"typography":{"fontSize":"18px"}}} -->
<p class="has-text-align-justify" style="font-size:18px">To assess and study the <strong>impact of Distributed Generation (DG), and the design of Microgrid Architecture in the Medium Voltage (MV) and Low Voltage (LV) networks</strong>, it is necessary to have advanced simulation tools and detailed models of the Distribution Network and its components. In order to make these simulations more accessible, open-source software tools such as<strong> OpenDSS</strong> (Open Distribution System Simulator) are now frequently used by Utilities and Research Laboratories across the globe.</p>
<!-- /wp:paragraph -->

![PROCESS](https://user-images.githubusercontent.com/112496588/188152646-b164f85c-dc40-430e-aaff-964d7405bba6.png)

<!-- wp:paragraph {"align":"justify"} -->
<p class="has-text-align-justify">However, simulation results with these tools highly depend on the quality and availability of network data (type, material, size and length of conductors, location and capacity of distribution transformers and capacitors) which is typically stored in the <strong>Geographical Information Systems (GIS)</strong> of power utilities. The necessary work to translate the GIS information to the respective power flow simulation tools is not only arduous but requires third party software packages to translate the data. In addition, any change in the database requires new iteration of data files exchanges among pieces of software which is proven to be tedious work when dealing with many distribution network feeders.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"justify"} -->
<p class="has-text-align-justify">This repository presents the implementation of <em><strong>QGIS2OPENDSS</strong>,</em> a plugin designed to automatically generate distribution network models for OpenDSS, which data comes directly from an open-source Geographic Information System (GIS) software environment, QGIS. This plugin was developed by researchers at the EPER Lab in the University of Costa Rica (UCR), and it’s part of a series of tools under development to help researchers and power engineers to assess the evolution of distributed generation and power systems, reducing the time from model to simulation by orders of magnitude (months to weeks)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"justify"} -->
<p class="has-text-align-justify">A working group has been created between PUCMM Researchers and EDENORTE´s Distribution, Planning and Network Study Department. The main objective of the group is to develop the processes and models to <em><strong>clean, fix, aggregate or remove incorrect, corrupted, incorrectly formatted, duplicated, or incomplete</strong></em> data within the GIS network dataset, in order to enable the data to be processed  by the <strong>QGIS2OPENDSS</strong> plugin in QGIS.</p>
<!-- /wp:paragraph -->

