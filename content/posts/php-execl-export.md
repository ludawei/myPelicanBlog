Title: thinkphp导出excel表格
Date: 2017-02-17
Tags: PHP
Category: PHP
Slug: php-excel-export

thinkphp导出execl表格
```php
public function testExcel()
{
    header('Content-Type:text/html;charset=utf-8');
    /*获取数据表内容*/
    $data = [["1", "2", "3"],
            ["1", "2", "3"],
            ["1", "2", "3"],
            ["1", "2", "3"]
    ];
    /*引入phpexcel包*/
    import('Vendor.phpexcel.PHPExcel');

    $phpexcel = new \PHPExcel();

    $sheet = $phpexcel->setActiveSheetIndex(0);

    foreach ($data as $k => $v) {
        $i = $k + 1;

        foreach ($v as $k1 => $v1) {
            $sheet->setCellValue( chr(65+$k1).$i, "$v1");
        }
    }
    // 生成2003excel格式的xls文件
    header('Content-Type: application/vnd.ms-excel');
    header('Content-Disposition: attachment;filename="01simple.xls"');
    header('Cache-Control: max-age=0');
    $objWriter = \PHPExcel_IOFactory::createWriter($phpexcel, 'Excel5');
    $objWriter->save('php://output');
    exit;
}
```
生成excel文件如下图：
![img](../images/php_excel_export.png)  

转自：<http://zhiqiexing.com/index.php/index/article/id/62.html>
