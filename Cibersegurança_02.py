port_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis"
}

def enumerate_services(ports):
    services = []
    for port in ports:
        if port in port_services:
            services.append(port_services[port])
        else:
            services.append("Desconhecido")
    return services

def main():
    ports_input = input()
    ports = [int(p.strip()) for p in ports_input.split(",")]
    services = enumerate_services(ports)
    print(services)

if __name__ == "__main__":
    main()
