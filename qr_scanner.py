# coding: utf-8
# Little dirty change in https://gist.github.com/omz/11891cb1c7ed459d34c7

from objc_util import *
from ctypes import c_void_p
import ui

found_codes = set()
main_view = None
s = None

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureMetadataOutput = ObjCClass('AVCaptureMetadataOutput')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')
dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = c_void_p


def captureOutput_didOutputMetadataObjects_fromConnection_(_self, _cmd, _output, _metadata_objects, _conn):
    global s
    objects = ObjCInstance(_metadata_objects)
    for obj in objects:
        s = str(obj.stringValue())
        if s:
            main_view.close()
            return

MetadataDelegate = create_objc_class('MetadataDelegate',
                                     methods=[captureOutput_didOutputMetadataObjects_fromConnection_],
                                     protocols=['AVCaptureMetadataOutputObjectsDelegate'])


@on_main_thread
def main():
    global main_view
    delegate = MetadataDelegate.new()
    main_view = ui.View(frame=(0, 0, 400, 400))
    main_view.name = 'QR Scanner'
    session = AVCaptureSession.alloc().init()
    device = AVCaptureDevice.defaultDeviceWithMediaType_('vide')
    _input = AVCaptureDeviceInput.deviceInputWithDevice_error_(device, None)
    if _input:
        session.addInput_(_input)
    else:
        print('Failed to create input')
        return
    output = AVCaptureMetadataOutput.alloc().init()
    queue = ObjCInstance(dispatch_get_current_queue())
    output.setMetadataObjectsDelegate_queue_(delegate, queue)
    session.addOutput_(output)
    output.setMetadataObjectTypes_(output.availableMetadataObjectTypes())
    prev_layer = AVCaptureVideoPreviewLayer.layerWithSession_(session)
    prev_layer.frame = ObjCInstance(main_view).bounds()
    prev_layer.setVideoGravity_('AVLayerVideoGravityResizeAspectFill')
    ObjCInstance(main_view).layer().addSublayer_(prev_layer)
    main_view.add_subview(label)
    session.startRunning()
    main_view.present('sheet')
    main_view.wait_modal()
    session.stopRunning()
    delegate.release()
    session.release()
    output.release()
    return s

if __name__ == '__main__':
    main()
