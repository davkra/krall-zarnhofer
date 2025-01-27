# Infrastruktur- und Konfigurationsmanagement

Template Konfigurationsdateien wurden erstellt und Konfigurationsdateien ins `.gitignore` übertragen. Dadurch sollten keine wichtigen Informationen wie Passwörter in das Git Repository gelangen.

Das Ansible Setup ist unter [setup.yml](../setup.yml) zu finden.

## Voraussetzungen

* Terraform installiert
* Ansible installiert
* SSH-Key erstellt und richtig konfiguriert

1. Konfigurationsdateien bearbeiten und credentials unter `.aws/` hinterlegen.
2. `terraform init`
3. `terraform plan`
4. `terraform apply`
5. `instance_public_ip` in `host.ini` übertragen
6. *(optional)* SSH-Verbidung testen: `ssh -i ~/.ssh/id_rsa ec2-user@<instance_public_ip>`
7. ansible-playbook -i hosts.ini setup.yml

`<instance_public_ip>:3000` im Browser eingeben um auf die Calculator App zuzugreifen.
