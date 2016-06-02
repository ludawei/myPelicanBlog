Title: MKMapView经纬度引起的一个bug
Date: 2016-06-02
Tags: iOS
Category: iOS
Slug: MKMapView经纬引起的一个bug
Summary: MKMapView边界经纬度引起的一个bug (解决方法)<br />原因应该是MKMapView默认的 纬度 范围是（-180 ~ 180），包含-180，但不包含180，故认为180的纬度是无效的。<br />解决方法就是将180变为-180（因为两者是相等的）

错误提示：
```
*** Terminating app due to uncaught exception 'NSInternalInconsistencyException', reason: 'An instance 0x139ce46f0 of class MyAnnotation was deallocated while key value observers were still registered with it. Current observation info: <NSKeyValueObservationInfo 0x139cc2820> (
<NSKeyValueObservance 0x139d5e110: Observer: 0x136c314b0, Key path: coordinate, Options: <New: NO, Old: YES, Prior: YES> Context: 0x0, Property: 0x139e30de0>
<NSKeyValueObservance 0x139d5e110: Observer: 0x136c314b0, Key path: coordinate, Options: <New: NO, Old: YES, Prior: YES> Context: 0x0, Property: 0x139e30de0>
)'
*** First throw call stack:
(0x18339ae38 0x1829fff80 0x18339ad80 0x183ceed50 0x1832923e8 0x18d9377a8 0x18d950300 0x18d967bc4 0x18d399050 0x18d365548 0x18d3658e8 0x18d3659f8 0x18d2f2f30 0x18d371910 0x18d35692c 0x18d6c70b8 0x185ed42f0 0x185ed41a4 0x183611e54 0x1833390e0 0x18335185c 0x183350f94 0x18334ecec 0x183278d10 0x184b60088 0x18854df70 0x10012372c 0x182e168b8)
libc++abi.dylib: terminating with uncaught exception of type NSException
```

解决方法：
```
if (anno.coordinate.longitude == 180)
{
    anno.coordinate = CLLocationCoordinate2DMake(anno.coordinate.latitude, -180);
}
```

原因应该是MKMapView默认的 纬度 范围是（-180 ~ 180），包含-180，但不包含180，故认为180的纬度是无效的。
解决方法就是将180变为-180（因为两者是相等的）
