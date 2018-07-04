<h2>Infrastructure as code</h2>

&nbsp; &nbsp;![alt text](https://github.com/hgolla-repos/kube-demo/blob/master/Orchestrator1.png)


<h2>Orchestrator/Configurator</h2>
Orchestrator/Configurator is the main auotmation engine to provision Microsoft Azure and GCP platforms by using terraform, ansible playbooks and Apache Libcloud. Definition files (Templates) in YAML  format contains Infrastructure configuration.

<h4> Terraform </h4> uses the meta data in configuration template file to deploy servers, configure Networks, Storage, Firewalls, LB etc., in automated fashion - cloud agnostic way
<h4> Ansible playbooks </h4> uses meta data in configuration template file and configures OS packages, services, application specific packages etc., Uses Apache libcloud to perform API operations - cloud agnostic way
<h4> Github </h4>
Automated code, configuration template files will be checked into source code control(github). When new commit submitted it will trigger CI/CD (in Jenkins) and run smoke tests in contained TEST infrastruture (Azure or GCP). Once verfied when all working on TEST enviromnement, code can be pushed into PROD. 

