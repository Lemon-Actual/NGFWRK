import time
import sys
import iperf3
import paramiko


###Configure SSH Paramaters###
ssh = paramiko.SSHClient()
###Accept missing key policy to auto accept###
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
###define Firewall IP or hostname, username and password for SSH connection###
ssh.connect('10.255.255.1',username='admin',password='password')

###Invoke SSH Shell####
channel = ssh.invoke_shell()

###This section is for configuring the associated firewall rule for traffic inspection###
###Modify this section with appropriate CLI command for device being adjusted###
###This specifically is for modifying a Fortigate on 6.4.2 Firmware and firewall rule 4###

###Configure Firewall Policy###
channel.send('conf firewall policy\n')
time.sleep(1)
###Edit Firewall policy that is inspecting traffic###
channel.send('edit 4\n')
time.sleep(1)
###Set Name of Firewall Rule###      
channel.send('set name "WAN to Inside"\n')
time.sleep(1)
###Set inspection mode (Proxy or Flow)###
channel.send('set inspection-mode flow\n')
time.sleep(1)
###Set SSL Inspection Mode###
channel.send('set ssl-ssh-profile no-inspection\n')
time.sleep(1)
###Set Antivirus inspection (unset to disable)###
channel.send('unset av-profile\n')
time.sleep(1)
###Set IPS inspection (unset to disable)####
channel.send('unset ips-sensor\n')
time.sleep(1)
###End commands to submit changes###
channel.send('end\n')
time.sleep(1)

###Close Connections###
channel.close
ssh.close


original_stdout = sys.stdout

###File to write perfomance output to###
with open('Fortibaseline.txt', 'w' ) as f:
    sys.stdout = f

###Call IPERF3###
    client = iperf3.Client()
    client.duration = 5
###IPERF3 Server hostname or address###
    client.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    client.port = 4444
###IPERF3 test protocol###
    client.protocol = 'tcp'


###IPERF3 test 1####
    print('Connecting to {0}:{1} over {2} for baseline test 1'.format(client.server_hostname, client.port, client.protocol))
    result = client.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 1 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
    
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)

###Call IPERF3###
    client2 = iperf3.Client()
    client2.duration = 5
###IPERF3 Server hostname or address###
    client2.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    client2.port = 4444
###IPERF3 test protocol###
    client2.protocol = 'tcp'



###IPERF3 test 2#### 
    print('Connecting to {0}:{1} over {2} for baseline test 2'.format(client2.server_hostname, client2.port, client2.protocol))
    result = client2.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 2 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True )
            time.sleep(5)

###Call IPERF3###
    client3 = iperf3.Client()
    client3.duration = 5
###IPERF3 Server hostname or address###
    client3.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    client3.port = 4444
###IPERF3 test protocol###
    client3.protocol = 'tcp'


###IPERF3 test 3####
    print('Connecting to {0}:{1} over {2} for baseline test 3'.format(client3.server_hostname, client3.port, client3.protocol))
    client3.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 3 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)



###Invoke SSH Shell####
channel = ssh.invoke_shell()


###This section is for configuring the associated firewall rule for traffic inspection###
###Modify this section with appropriate CLI command for device being adjusted###
###This specifically is for modifying a Fortigate on 6.4.2 Firmware and firewall rule 4###


###Configure Firewall Policy###
channel.send('conf firewall policy\n')
time.sleep(1)
###Edit Firewall policy that is inspecting traffic###
channel.send('edit 4\n')
time.sleep(1)
###Set Name of Firewall Rule###      
channel.send('set name "WAN to Inside"\n')
time.sleep(1)
###Set inspection mode (Proxy or Flow)###
channel.send('set inspection-mode proxy\n')
time.sleep(1)
###Set SSL Inspection Mode###
channel.send('set ssl-ssh-profile no-inspection\n')
time.sleep(1)
###Set Antivirus inspection (unset to disable)###
channel.send('unset av-profile\n')
time.sleep(1)
###Set IPS inspection (unset to disable)####
channel.send('unset ips-sensor\n')
time.sleep(1)
###End commands to submit changes###
channel.send('end\n')
time.sleep(1)

###Close Connections###
channel.close
ssh.close



###File to write perfomance output to###
with open('FortiProxybaseline.txt', 'w' ) as f:
    sys.stdout = f


###Call IPERF3###
    client = iperf3.Client()
    client.duration = 5
###IPERF3 Server hostname or address###
    client.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    client.port = 4444
###IPERF3 test protocol###
    client.protocol = 'tcp'



###IPERF3 test 1####
    print('Connecting to {0}:{1} over {2} for Proxy baseline test 1'.format(client.server_hostname, client.port, client.protocol))
    result = client.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 1 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
    
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)

###Call IPERF3###
    client2p = iperf3.Client()
    client2p.duration = 5
###IPERF3 Server hostname or address###
    client2p.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    client2p.port = 4444
###IPERF3 test protocol###
    client2p.protocol = 'tcp'
 
###IPERF3 test 2#### 
    print('Connecting to {0}:{1} over {2} for Proxy baseline test 2'.format(client2p.server_hostname, client2p.port, client2p.protocol))
    result = client2p.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 2 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)

###Call IPERF3###
    client3 = iperf3.Client()
    client3.duration = 5
###IPERF3 Server hostname or address###
    client3.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    client3.port = 4444
###IPERF3 test protocol###
    client3.protocol = 'tcp'


###IPERF3 test 3####
    print('Connecting to {0}:{1} over {2} for Proxy baseline test 3'.format(client3.server_hostname, client3.port, client3.protocol))
    result = client3.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 3 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)





###Configure firewall to enable proxy and AV inspection###

###Invoke SSH Shell####
channel = ssh.invoke_shell()


###This section is for configuring the associated firewall rule for traffic inspection###
###Modify this section with appropriate CLI command for device being adjusted###
###This specifically is for modifying a Fortigate on 6.4.2 Firmware and firewall rule 4###

###Configure Firewall Policy###
channel.send('conf firewall policy\n')
time.sleep(1)
###Edit Firewall policy that is inspecting traffic###
channel.send('edit 4\n')
time.sleep(1)
###Set Name of Firewall Rule###      
channel.send('set name "WAN to Inside"\n')
time.sleep(1)
###Set inspection mode (Proxy or Flow)###
channel.send('set inspection-mode proxy\n')
time.sleep(1)
###Set SSL Inspection Mode###
channel.send('set ssl-ssh-profile no-inspection\n')
time.sleep(1)
###Set Antivirus inspection (unset to disable)###
channel.send('set av-profile default\n')
time.sleep(1)
###Set IPS inspection (unset to disable)####
channel.send('unset ips-sensor\n')
time.sleep(1)
###End commands to submit changes###
channel.send('end\n')
time.sleep(1)

###Close Connections###
channel.close
ssh.close


###Perform Baseline with Firewall in Proxy Mode with AV Enabled###



###File to write perfomance output to###
with open('FortibaselinePAV.txt', 'w' ) as f:
    sys.stdout = f

###Call IPERF3###
    clientAV = iperf3.Client()
    clientAV.duration = 5
###IPERF3 Server hostname or address###
    clientAV.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    clientAV.port = 4444
###IPERF3 test protocol###
    clientAV.protocol = 'tcp'


###IPERF3 test 1####
    print('Connecting to {0}:{1} over {2} for baseline test 1'.format(clientAV.server_hostname, clientAV.port, clientAV.protocol))
    result = clientAV.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 1 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
    
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)

###Call IPERF3###
    clientAV2 = iperf3.Client()
    clientAV2.duration = 5
###IPERF3 Server hostname or address###
    clientAV2.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    clientAV2.port = 4444
###IPERF3 test protocol###
    clientAV2.protocol = 'tcp'



###IPERF3 test 2#### 
    print('Connecting to {0}:{1} over {2} for baseline test 2'.format(clientAV2.server_hostname, clientAV2.port, clientAV2.protocol))
    result = clientAV2.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 2 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True )
            time.sleep(5)

###Call IPERF3###
    clientAV3 = iperf3.Client()
    clientAV3.duration = 5
###IPERF3 Server hostname or address###
    clientAV3.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    clientAV3.port = 4444
###IPERF3 test protocol###
    clientAV3.protocol = 'tcp'


###IPERF3 test 3####
    print('Connecting to {0}:{1} over {2} for baseline test 3'.format(clientAV3.server_hostname, clientAV3.port, clientAV3.protocol))
    clientAV3.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 3 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)




###Configure Firewall Policy for Proxy Mode with AV and IPS Enabled###

###Invoke SSH Shell####
channel = ssh.invoke_shell()


###This section is for configuring the associated firewall rule for traffic inspection###
###Modify this section with appropriate CLI command for device being adjusted###
###This specifically is for modifying a Fortigate on 6.4.2 Firmware and firewall rule 4###


###Configure Firewall Policy###
channel.send('conf firewall policy\n')
time.sleep(1)
###Edit Firewall policy that is inspecting traffic###
channel.send('edit 4\n')
time.sleep(1)
###Set Name of Firewall Rule###      
channel.send('set name "WAN to Inside"\n')
time.sleep(1)
###Set inspection mode (Proxy or Flow)###
channel.send('set inspection-mode proxy\n')
time.sleep(1)
###Set SSL Inspection Mode###
channel.send('set ssl-ssh-profile no-inspection\n')
time.sleep(1)
###Set Antivirus inspection (unset to disable)###
channel.send('set av-profile default\n')
time.sleep(1)
###Set IPS inspection (unset to disable)####
channel.send('set ips-sensor default\n')
time.sleep(1)
###End commands to submit changes###
channel.send('end\n')
time.sleep(1)

###Close Connections###
channel.close
ssh.close


###Perform Baseline with Firewall in Proxy Mode with AV Enabled###



###File to write perfomance output to###
with open('FortibaselinePAVIPS.txt', 'w' ) as f:
    sys.stdout = f

###Call IPERF3###
    clientPAVIPS = iperf3.Client()
    clientPAVIPS.duration = 5
###IPERF3 Server hostname or address###
    clientPAVIPS.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    clientPAVIPS.port = 4444
###IPERF3 test protocol###
    clientPAVIPS.protocol = 'tcp'


###IPERF3 test 1####
    print('Connecting to {0}:{1} over {2} for baseline test 1'.format(clientPAVIPS.server_hostname, clientPAVIPS.port, clientPAVIPS.protocol))
    result = clientPAVIPS.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 1 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
    
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)

###Call IPERF3###
    clientPAVIPS2 = iperf3.Client()
    clientPAVIPS2.duration = 5
###IPERF3 Server hostname or address###
    clientPAVIPS2.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    clientPAVIPS2.port = 4444
###IPERF3 test protocol###
    clientPAVIPS2.protocol = 'tcp'



###IPERF3 test 2#### 
    print('Connecting to {0}:{1} over {2} for baseline test 2'.format(clientPAVIPS2.server_hostname, clientPAVIPS2.port, clientPAVIPS2.protocol))
    result = clientPAVIPS2.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 2 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True )
            time.sleep(5)

###Call IPERF3###
    clientPAVIPS3 = iperf3.Client()
    clientPAVIPS3.duration = 5
###IPERF3 Server hostname or address###
    clientPAVIPS3.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    clientPAVIPS3.port = 4444
###IPERF3 test protocol###
    clientPAVIPS3.protocol = 'tcp'


###IPERF3 test 3####
    print('Connecting to {0}:{1} over {2} for baseline test 3'.format(clientPAVIPS3.server_hostname, clientPAVIPS3.port, clientPAVIPS3.protocol))
    clientPAVIPS3.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 3 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)





###Configure Firewall Policy for Proxy Mode with AV IPS and Cert inspection Enabled###

###Invoke SSH Shell####
channel = ssh.invoke_shell()

###This section is for configuring the associated firewall rule for traffic inspection###
###Modify this section with appropriate CLI command for device being adjusted###
###This specifically is for modifying a Fortigate on 6.4.2 Firmware and firewall rule 4###

###Configure Firewall Policy###
channel.send('conf firewall policy\n')
time.sleep(1)
###Edit Firewall policy that is inspecting traffic###
channel.send('edit 4\n')
time.sleep(1)
###Set Name of Firewall Rule###      
channel.send('set name "WAN to Inside"\n')
time.sleep(1)
###Set inspection mode (Proxy or Flow)###
channel.send('set inspection-mode proxy\n')
time.sleep(1)
###Set SSL Inspection Mode###
channel.send('set ssl-ssh-profile certificate-inspection\n')
time.sleep(1)
###Set Antivirus inspection (unset to disable)###
channel.send('set av-profile default\n')
time.sleep(1)
###Set IPS inspection (unset to disable)####
channel.send('set ips-sensor default\n')
time.sleep(1)
###End commands to submit changes###
channel.send('end\n')
time.sleep(1)

###Close Connections###
channel.close
ssh.close


###Perform Baseline with Firewall in Proxy Mode with AV IPS And Cert Inspection Enabled###


###File to write perfomance output to###
with open('FortibaselinePAVIPSC.txt', 'w' ) as f:
    sys.stdout = f

###Call IPERF3###
    clientPAVIPSC = iperf3.Client()
    clientPAVIPSC.duration = 5
###IPERF3 Server hostname or address###
    clientPAVIPSC.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    clientPAVIPSC.port = 4444
###IPERF3 test protocol###
    clientPAVIPSC.protocol = 'tcp'


###IPERF3 test 1####
    print('Baseline Firewall Test With Proxy Mode, AV, IPS, and Cert Inspection Enabled')
    print('Connecting to {0}:{1} over {2} for baseline test 1'.format(clientPAVIPSC.server_hostname, clientPAVIPSC.port, clientPAVIPSC.protocol))
    result = clientPAVIPSC.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 1 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
    
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)

###Call IPERF3###
    clientPAVIPSC2 = iperf3.Client()
    clientPAVIPSC2.duration = 5
###IPERF3 Server hostname or address###
    clientPAVIPSC2.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    clientPAVIPSC2.port = 4444
###IPERF3 test protocol###
    clientPAVIPSC2.protocol = 'tcp'



###IPERF3 test 2#### 
    print('Connecting to {0}:{1} over {2} for baseline test 2'.format(clientPAVIPSC2.server_hostname, clientPAVIPSC2.port, clientPAVIPSC2.protocol))
    result = clientPAVIPSC2.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 2 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True )
            time.sleep(5)

###Call IPERF3###
    clientPAVIPSC3 = iperf3.Client()
    clientPAVIPSC3.duration = 5
###IPERF3 Server hostname or address###
    clientPAVIPSC3.server_hostname = '10.255.255.1'
###IPERF3 Server Port###    
    clientPAVIPSC3.port = 4444
###IPERF3 test protocol###
    clientPAVIPSC3.protocol = 'tcp'


###IPERF3 test 3####
    print('Connecting to {0}:{1} over {2} for baseline test 3'.format(clientPAVIPSC3.server_hostname, clientPAVIPSC3.port, clientPAVIPSC3.protocol))
    clientPAVIPSC3.run()

    if result.error:
            print(result.error)
    else:
            print('')
            print('Test 3 completed:')
            print('  bytes transmitted  {0}'.format(result.sent_bytes))
            print('')
            print('Average sent data:')
            print('  bits per second      (bps)   {0}'.format(result.sent_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))
            print('')
            print('Average received data:')
            print('  bits per second      (bps)   {0}'.format(result.received_bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
            print('', flush=True)
            time.sleep(5)

sys.stdout = original_stdout

















