import rest

class DogGateway:
    
    def __init__(self, url):
        
        #remove trailing slashes
        if(url[-1]=='/'):
            url = url[:-1]
        
        #store the base api url
        self.url = url
        
        #build the devices url
        self.all_devices_url = self.url+"/devices"
        
     
    def getAllDevices(self):

        return rest.send(url = self.all_devices_url, headers = {'Accept':'application/json'})
    
    def sendCommand(self, device_id, command, parameters = {}):

        #print 'sending: '+self.all_devices_url+'/'+device_id+'/commands/'+command
        rest.send('PUT', self.all_devices_url+'/'+device_id+'/commands/'+command, str(parameters), 
                  {'Accept':'application/json', 'Content-Type':'application/json'})
        
    def getStatus(self,device_id):

        #print 'Sending: '+self.all_devices_url+'/'+device_id+'/status'
        return rest.send(url = self.all_devices_url+'/'+device_id+'/status')

    def getDevicesOfType(self, device_type):

        devices = {}
        
        all_devices = self.getAllDevices()
        
        # iterate over all devices
        for i in range(0, len(all_devices['devices'])):
            #get the device class
            device_class =  all_devices['devices'][i]['class']
            
            #check the device class
            if(device_class == device_type):
            
                #get the device id
                device_id = all_devices['devices'][i]['id']
            
                #store the devices
                devices[device_id]=all_devices['devices'][i]
        
        #return the extracted devices
        return devices
