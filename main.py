import time
import sys


animation = "|/-\\"

for i in range(26):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print ("loading...")
time.sleep(2.5)
print ("[   0.553817]  [<ffffffffb8e9aa1f>] ret_from_fork+0x1f/0x40")
print ("[   0.553858]  [<ffffffffb8e8d2a8>] ? rest_init+0x88/0x88")
print ("[   0.553932] Kernel Offset: 0x37600000 from 0xffffffff81000000 (relocation range: 0xffffffff80000000-0xffffffffbffffff)")
print ("[   0.553991] ---[ end Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,8)]")
time.sleep(10)
