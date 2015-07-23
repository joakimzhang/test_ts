#-*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import collections
class TS_analysis():
    def __init__(self,file_path):
    
        self.pak_size = 188
        # 创建图表1
        plt.figure(1)
        self.file_path=r'%s'%file_path.decode('utf8')
        self.TS_file = open(self.file_path, 'rb')
        self.offset_tmp=0
        self.pts_x=[]
        self.pts_y=[]
        self.pts_x_y=[]
        self.PMT_PID=[]
        self.program_PID={}
            
    def show_PID_pic(self):
        plt.figure(1)
        plt.plot(self.pts_x,self.pts_y)
        #plt.vlines(self.pts_x,[0],self.pts_y)
        plt.show()
    def get_sync_head(self):
        ''''得到188个字节TS包的同步头'''
        for self.pak_size in [188,204,214]:
            print "~~~~~~~~~~~~~~~~~~~pak_size is %d"%self.pak_size
            for i in range(0,188):
                section = self.TS_file.read(self.pak_size)
                #print "section[0]",ord(section[0])
                for c in range (len(section)):                   
                    if ord(section[c]) == 0x47:
                        self.offset_tmp+=c
                        #print "offset_tmp:%d"%self.offset_tmp    
                        break
                print "self.offset_temp is %s"%self.offset_tmp
                self.TS_file.seek(self.offset_tmp,0)   
                
                for j in range(self.pak_size):
                    section = self.TS_file.read(self.pak_size)
                    if ord(section[0]) == 0x47:
                        
                        if j==187:
                            print "check the offset successfully for %d times!!"%self.pak_size
                            return 1
                        print "get the offset successfully for %d times!!"%j
                        continue
                    else:
                        self.offset_tmp+=1
                        self.TS_file.seek(self.offset_tmp,0)
                        break  
            print "return 0"
            
        return 0
    
    def get_PMT_PID(self):
        
        for i in range (50000):
            section = self.TS_file.read(self.pak_size)
            if len(section) == self.pak_size:
                PID = (ord(section[1]) & 0x1F)<<8 | ord(section[2])
                field_control = (ord(section[3])>>4 & 0x3)
                #print field_control
                payload_start = (ord(section[1])>>6 & 0x1)
                
                if payload_start == 1 and (PID == 0):
                    #print "payload_start is not 0 is %d"%payload_start
                    
                    if field_control == 1 :
                        #当payload_start=1 时候，TS头部后面的第一个字节的值代表调整字段的长度，这里是0，加上这个字节本身，调整字段为1个字节
                        t_filed = ord(section[4])+1
                        
                        
                        section_length = (ord(section[1+t_filed+4]) & 0x0F) << 8 | ord(section[2+t_filed+4])
                        for i in range(0,section_length-12,4):
                            program_number = ord(section[8+t_filed+4+i]) << 8 | ord(section[9+t_filed+4+i])
                            #print "program number is %d"%program_number
                            #print i
                            if program_number !=0:
                                program_map_PID = (ord(section[10+t_filed+4+i]) & 0x1F) << 8 | ord(section[11+t_filed+4+i])
                                #print program_map_PID
                                #if program_map_PID==program_number:
                                self.PMT_PID.append(program_map_PID)
                        print self.PMT_PID
                        if len(self.PMT_PID):
                            break
                                
                    else:
                        print "field control is not 1"
                        
    def get_programe_PID(self):
        
        print self.PMT_PID
        for i in range (50000):
            section = self.TS_file.read(self.pak_size)
            if len(section) == self.pak_size:
                PID = (ord(section[1]) & 0x1F)<<8 | ord(section[2])
                field_control = (ord(section[3])>>4 & 0x3)
                payload_start = (ord(section[1])>>6 & 0x1)
                
                if PID in self.PMT_PID:
                    pid_dic={2:'v',4:'a'}
                    tmp_dic={}
                    if payload_start != 0:
                        #print "payload_start is not 0 is %d"%payload_start
                        
                        if field_control == 1:
                            #print "field_control is 1,the PMT PID is%d"%PID
                            #当payload_start=1 时候，TS头部后面的第一个字节的值代表调整字段的长度，这里是0，加上这个字节本身，调整字段为1个字节
                            t_filed = ord(section[4])+1
                            #print t_filed
                            #print ord(section[t_filed+4])
                            #program_number = ord(section[8+t_filed+4]) << 8 | ord(section[9+t_filed+4])
                           
                            section_length = (ord(section[1+t_filed+4]) & 0x0F) << 8 | ord(section[2+t_filed+4])
                            program_info_length = (ord(section[10+t_filed+4]) & 0x0F) << 8 | ord(section[11+t_filed+4])
                            #print "section_length is %d"%section_length
                            #print "program_info_length is %d"%program_info_length
                            pos = 12
                            if program_info_length != 0:
                                pos += program_info_length
                            for i in range(pos,section_length+2-4,5):
                                programe_type = ord(section[i+t_filed+4])
                                programe_PID = ((ord(section[t_filed+4+i+1]) << 8) | ord(section[t_filed+4+i+2])) & 0x1FFF
                                ES_info_length  = (((ord(section[t_filed+4+i+3])&0x0F) << 8) | ord(section[t_filed+4+i+4]))
                                #print "the programe_PID is %d"%programe_PID
                                #print "the programe type is %d"%programe_type
                                #print "the PMT PID is %d"%PID
                                #print "the es info length is %d"%ES_info_length
                                if programe_type in [2,4]: 
                                    #tmp_list.append(programe_PID)
                                    tmp_dic[pid_dic[programe_type]]=programe_PID
                            if len(tmp_dic):
                                self.program_PID[PID]=tmp_dic
                            if ES_info_length !=0:
                                print "~~~~~~~~the ES_info_length is not 0,the PMT include es info!!!!!!"

                        else:
                            print "field control is not 1"
                
        print self.program_PID
        return self.program_PID
            #if len(self.program_PID):
            #break
    def get_pid_pts(self,audio_pid,video_pid):  
        print "~~~~~~~the audio is :%s"%audio_pid
        print "~~~~~the audio is :%s"%video_pid
        print os.getcwd()
        file_list = os.listdir(os.getcwd())
        print file_list
                     
        total_pid = dict()
        
        section = self.TS_file.read(self.pak_size)
        #print "section type is %s"%section
        pts_p=0
        dts_p=0
        pts=0
        dts=0

        p_num=0
        PID_p=0
        for i in range (50000):
            if len(section) == self.pak_size:
                PID = (ord(section[1]) & 0x1F)<<8 | ord(section[2])
                field_control = (ord(section[3])>>4 & 0x3)
                
                payload_start = (ord(section[1])>>6 & 0x1)
                
                #解析 PTS
                if payload_start != 0 and (PID == int(audio_pid) or PID == int(video_pid)):
                    if field_control == 1 :
                        pts_tag = (ord(section[11])>>6)
                        if pts_tag == 3:
                            pts = ((ord(section[13])>>1) & 0x03)<<30 | ord(section[14])<<22 | (ord(section[15])>>1)<<15 | ord(section[16])<<7 | ord(section[17])>>1
                        #pts = (ord(section[9]))
                            dts = ((ord(section[18])>>1) & 0x03)<<30 | ord(section[19])<<22 | (ord(section[20])>>1)<<15 | ord(section[21])<<7 | ord(section[22])>>1
                        elif pts_tag == 2:
                            pts = ((ord(section[13])>>1) & 0x03)<<30 | ord(section[14])<<22 | (ord(section[15])>>1)<<15 | ord(section[16])<<7 | ord(section[17])>>1
                        else:
                            print "error!!!!!pts_tag is not 2 or 3 it is %d" % pts_tag

                        if pts_p != 0 and PID_p < PID:
                            print "the pts substitude is %d" %((pts-pts_p)/90)
                            self.pts_y.append((pts-pts_p)/90)
                            self.pts_x.append(p_num)
                            self.pts_x_y.append((p_num,(pts-pts_p)/90))
                            p_num+=1
                            print self.pts_x
                            print self.pts_y
                            print self.pts_x_y
                            
                        if dts_p != 0:
                            print "the dts substitude is %d" %((dts-dts_p)/90)
                        pts_p=pts
                        dts_p=dts
                        PID_p=PID
                        
                    if field_control == 3:
                        pts_tag = (ord(section[11+ord(section[4])+1])>>6)
                        if pts_tag == 3:
                            pts = ((ord(section[13+ord(section[4])+1])>>1) & 0x03)<<30 | ord(section[14+ord(section[4])+1])<<22 | (ord(section[15+ord(section[4])+1])>>1)<<15 | ord(section[16+ord(section[4])+1])<<7 | ord(section[17+ord(section[4])+1])>>1
                            dts = ((ord(section[18+ord(section[4])+1])>>1) & 0x03)<<30 | ord(section[19+ord(section[4])+1])<<22 | (ord(section[20+ord(section[4])+1])>>1)<<15 | ord(section[21+ord(section[4])+1])<<7 | ord(section[22+ord(section[4])+1])>>1
                        elif pts_tag == 2:
                            pts = ((ord(section[13+ord(section[4])+1])>>1) & 0x03)<<30 | ord(section[14+ord(section[4])+1])<<22 | (ord(section[15+ord(section[4])+1])>>1)<<15 | ord(section[16+ord(section[4])+1])<<7 | ord(section[17+ord(section[4])+1])>>1
                        else:
                            print "error!!!!!pts_tag is not 2 or 3 is:%d" % pts_tag

                        if pts_p != 0 and PID_p < PID:
                            print "the pts substitude is %d" %((pts-pts_p)/90)
                            self.pts_y.append((pts-pts_p)/90)
                            self.pts_x.append(p_num)
                            self.pts_x_y.append((p_num,(pts-pts_p)/90))
                            print self.pts_x
                            print self.pts_y
                            print self.pts_x_y
                            p_num+=1
                            
                        if dts_p != 0:
                            print "the dts substitude is %d" %((dts-dts_p)/90)
                        pts_p=pts
                        dts_p=dts
                        PID_p=PID

                #for key in total_pid.keys():
                #    if PID == key:
                #        total_pid[key] = total_pid[key] + 1
                #        break
                #else:
                #    total_pid[PID] = 1
                
                section = self.TS_file.read(self.pak_size)
            
        #total_pid = [(j,total_pid[j]) for j in sorted([i for i in total_pid.keys()])]
        #print total_pid
        self.TS_file.close()
    
if __name__ == "__main__":
    #test_path=r'\\bjfile02\BJShare\Department\FAE\Soc\AVL8332\Stream\DTMB\山东\青岛文广\AVS播放不同步\KingVonTs_722_001.ts'
    #test_path=r'\\bjfile02\BJShare\Department\FAE\Soc\Yangtze\stream\晋中榆次\586\KingVonTs_586_001.ts'
    #test_path=r'\\bjfile02\BJShare\Department\FAE\Soc\Yangtze\stream\晋中榆次\586\KingVonTs_586_001.ts'.decode('utf8')
    #test_path=r'\\BJFile02\BJShare\Department\FAE\Soc\AVL8332\Stream\DTMB\迎威科技音视频不同步\迎威科技音视频不同步KingVonTs_123_002.ts'.decode('utf8')

    #test_path=r'\\bjfile02\BJShare\Department\FAE\Soc\AVL8332\Stream\DTMB\山东\青岛文广\AVS播放不同步\KingVonTs_722_001.ts'.decode('utf8')
    #test_path=r'\\bjfile02\BJShare\Department\FAE\Soc\AVL8332\Stream\DTMB\山东\青岛文广\AVS播放不同步\KingVonTs_722_001.ts'.decode('utf8')
    test_path=r'\\Bjserver4\streams\Lib_test_stream\Video\BJ_DTMB_H264_546MHz_1.ts'.decode('utf8')
    #test_path=r'\\bjfile02\BJShare\Department\FAE\Soc\AVL8332\Stream\DTMB\河北\涞水\涞水KingVonTs_698_001.ts'.decode('utf8')

    
    
    
    test_object=TS_analysis(test_path)
    test_PID=0
    test_PID=test_object.get_sync_head()
    print "PID:%d"%test_PID
    if test_PID != 0:
        print "get PID successful:%d"%test_PID
        #test_object.get_pid(64 ,65)
        test_object.get_PMT_PID()
        test_object.get_programe_PID()
        #for i,j in test_object.program_PID.values():
         #   print i,j
            #test_object.get_pid(i,j)
        
        #self.program_PID[PID]
        #test_object.show_PID_pic()
    else:
        print "get PID fail"
