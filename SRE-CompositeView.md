<h2>Infrastructure as code</h2>

&nbsp; &nbsp;![alt text](https://github.com/hgolla-repos/kube-demo/blob/master/Orchestrator1.png)


<h2>Orchestrator/Configurator</h2>
Orchestrator/Configurator is the main auotmation engine (Python) to provision Microsoft Azure and GCP platforms by using terraform, ansible playbooks and Apache Libcloud. Definition files (Templates) in YAML  format contains Infrastructure configuration.

<h4> Terraform </h4> uses the meta data in configuration template file to deploy servers, configure Networks, Storage, Firewalls, LB etc., in automated fashion - cloud agnostic way
<h4> Ansible playbooks </h4> uses meta data in configuration template file and configures OS packages, services, application specific packages etc., Uses Apache libcloud to perform API operations - cloud agnostic way
<h4> Github </h4>
Automated code, configuration template files will be checked into source code control(github). When new commit submitted it will trigger CI/CD (in Jenkins) and run smoke tests in contained TEST infrastruture (Azure or GCP). Once verfied when all working on TEST enviromnement, code can be pushed into PROD. 

<h2>Monitoring</h2>
<h4>High-level overview of monitoring Cloud Infrastructure with Prometheus </h4>

&nbsp; &nbsp;![alt text](https://github.com/hgolla-repos/kube-demo/blob/master/Monitor.png)

<h4>Prometheus</h4>
-  is an open-source monitoring system that collects metrics from your services and stores them in a time-series database. 
<h4>node_exporter</h4>
- This produces metrics about infrastructure, including the current CPU, memory and disk usage, as well as I/O and network statistics, such as the number of bytes read from a disk or a server's average load.
<h4>mysqld_exporter</h4>
- This gathers metrics related to a MySQL server, such as the number of executed queries, average query response time, and cluster replication status.
<h4>Other_exporters</h4>
- Examples RabbitMQ, nginx etc.,
<h4>SRE-custom_exporters</h4>
- Any Custom services deployed by SRE team will forward metrics/alerts to Prometheus
<h4>Nginx</h4>
-  to terminate SSL and provide authentication for Prometheus
<h4>Grafana</h4>
- Dashboard to view metrics (data visualization tool)
<h4>Alertmanager</h4>
-  is a tool for processing alerts, which de-duplicates, groups, and sends alerts to the appropriate receiver. It can handle alerts from client applications such as Prometheus, and it supports many receivers including e-mail, PagerDuty and Slack.
