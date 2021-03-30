import sys
import time
class parking:
    S_count = 0
    L_count = 0
    M_count = 0
    slot_id = 0
    id = "0"
    t = "V"
    slot_id = 0
    slot = []
    slot[0:9] = ['S'] * 10
    slot[10:16] = ['M'] * 7
    slot[17:19] = ['L'] * 3
    def vehicle_details(self):
        parking.id = str(input("Please Enter Vehicle ID"))
        parking.t = str(input("Vehicle Type eg: S- Motor Bike M- Car L- Bus"))
        parking.slot_id += 1
        if parking.t == 'S':
            parking.S_count += 1
        elif parking.t == 'M' or (parking.S_count>10 and parking.t == 'S'):
            parking.M_count += 1
        elif parking.t == 'L' or (parking.S_count>10 and parking.t == 'S') or (parking.M_count>10 and parking.t == 'M'):
            parking.L_count += 1
    def capacity(self):
        if parking.slot_id > 19:
            print("oops!!!! PARKING SLOT NOT AVAILABLE")
            time.sleep(2)
    def fill_slot(self,slot_id,vehicleid,vtype):
        parking.slot.pop((slot_id))
        parking.slot.insert((slot_id), {slot_id: [vehicleid, vtype]})
        print(parking.slot)
        self.show()
    def show(self):
        print("\n\n##################")
        print("Vehicle ID:{0}\nVehicle Type: {1}\nSlot ID: {2}".format(parking.id,parking.t,parking.slot_id))
        print("##################\n\n")
        time.sleep(3)
    def end_parking(self,v_id,v_type,s_id):
        #print(parking.slot,len(parking.slot))
        if s_id < 10:
            n = 'S'
        elif s_id >= 10 or s_id < 17:
            n = 'M'
        else:
            n = 'L'
        d = parking.slot.pop(s_id-1)
        print(d)
        print(parking.slot)
        parking.slot.insert(s_id-1,n)
        #print(parking.slot, len(parking.slot))
        v = list(d.values())
        k = list(d.keys())
        print("\n\n###########################")
        print("End parking: SUCCESS\n\nVehicle ID: {0}\nVehicle Type: {1}\nSlot ID: {2}\n\n\n".format(v[0][0],v[0][1],k[0]))
        print("###########################\n\n")
        time.sleep(2)
count = 0

while(1):
    option = int(input("Enter option \n1. Check Availability \n2. End Parking \n3. Exit\n"))
    p = parking()
    if option == 1:
        t = str(input("Enter Vehicle Type (S-Motor Cycle,M-Car,L-Bus)"))
        p.vehicle_details()
        if t == 'S':
            if 'S' in parking.slot or 'M' in parking.slot or 'L' in parking.slot:
                print("Slot Available\n")
                print("Entered details id {0} type {1}".format(p.id,p.t))
                if 'S' in parking.slot:
                    s = parking.slot.index(t)
                    p.fill_slot(s,p.id,t)
                else:
                    if 'M' in parking.slot:
                        s = parking.slot.index('M')
                        p.fill_slot(s,p.id,t)
                    else:
                        s = parking.slot.index('L')
                        p.fill_slot(s, p.id,t)

            else:
                p.capacity()

        elif t == 'M':
            if 'M' in parking.slot:
                s = p.slot.index('M')
                p.fill_slot(s,p.id,t)
            elif 'L' in parking.slot:
                s = p.slot.index('L')
                p.fill_slot(s,p.id,t)
            else:
                print("oops!!!! PARKING SLOT NOT AVAILABLE")
                time.sleep(2)
        elif t == 'L':
            if 'L' in parking.slot:
                s = p.slot.index('L')
                p.fill_slot(s,p.id,t)
            else:
                print("oops!!!! PARKING SLOT NOT AVAILABLE")
                time.sleep(2)
        else:
            print("Please Enter a valid vehicle Type")
            time.sleep(2)
    elif option == 2:
        id = input("Please Enter vehicle id")
        t = str(input("Please enter vehicle type"))
        s_id = int(input("Please Enter parking slot id"))
        p.end_parking(id,t,s_id)
    elif option == 3:
        sys.exit()
    else:
        print("Please Enter a valid option")
        time.sleep(2)