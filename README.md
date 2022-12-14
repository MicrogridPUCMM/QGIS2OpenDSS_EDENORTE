# QGIS2OpenDSS_EDENORTE

See full publication:  https://microgrid.pucmm.edu.do/modeling-of-distribution-networks-with-high-renewables-penetration-in-open-source-software-opendss-qgis/

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
<p class="has-text-align-justify">This repository presents the implementation of <em><strong>QGIS2OPENDSS</strong>,</em> a plugin designed to automatically generate distribution network models for OpenDSS, which data comes directly from an open-source Geographic Information System (GIS) software environment, QGIS. This plugin was developed by researchers at the EPER Lab in the University of Costa Rica (UCR), and it???s part of a series of tools under development to help researchers and power engineers to assess the evolution of distributed generation and power systems, reducing the time from model to simulation by orders of magnitude (months to weeks)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"justify"} -->
<p class="has-text-align-justify">A working group has been created between PUCMM Researchers and EDENORTE??s Distribution, Planning and Network Study Department. The main objective of the group is to develop the processes and models to <em><strong>clean, fix, aggregate or remove incorrect, corrupted, incorrectly formatted, duplicated, or incomplete</strong></em> data within the GIS network dataset, in order to enable the data to be processed?? by the <strong>QGIS2OPENDSS</strong> plugin in QGIS.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Repository content</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Update (02-09-2022)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>QGIS version:</strong> QGIS 3.18.3<br><strong>QGIS2OpenDSS version</strong>: <a href="https://drive.google.com/drive/folders/1-5cYZdKdgDeJs1S0SwUIKKDuGMBl-Vnj?usp=sharing">Modified by PUCMM Team</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Content:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There are 3 folders:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><strong>DSSAGO30 </strong>- Contains a sample of available residential, commercial, and industrial load profiles.</li><li><strong>GISAGO30 </strong>- Contains the GIS Layers:<br><br><ul><li>BT AEREA</li></ul><ul><li>MT AREA</li></ul><ul><li>MT AEREA</li></ul><ul><li>MT SOTERRADA</li></ul><ul><li>TRANSFORMADORES</li></ul><ul><li>SUBESTACI??N</li></ul><ul><li>PV<br><br></li></ul></li><li><strong>QGIS2OPENDSS_AGO30/TEST1708 ??? </strong>Contains the output files of the QGIS2OpenDSS for the modelled circuit. VOLG101.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Limitations - </strong>Update (02-09-2022)</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>There is no commercial nor industrial loads in these model</li><li>There are ~150 transformers with no load connection (missing data).</li><li>PV Layer is missing PVProfile and PVTemp curves</li></ul><ul><li>Data Dictionaries and Guidelines need to be updated to reflect lastest changes</li>
<!-- /wp:list -->



