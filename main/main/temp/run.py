from main.models.po_model import POModel

data = """
TLT-PO-01-0221;H105025407KMH;H105025407;9432612856;H105025407;DLLA150SM407;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;48; 15.38 ;738.24;1.1; 415,644.50 ; 500,000 ; 550,000 ;T5;;
TLT-PO-01-0221;94136100133YL;9413610013;9413610013;131152-1420;A138;3YL;pump element;Ty bơm cao áp;Ty bơm cao áp;36; 15.42 ;555.12;1.1; 416,725.50 ; 500,000 ; 550,000 ;co san ;;
TLT-PO-01-0221;94436102103YL;9443610210;9443610210;131152-5520;A186;3YL;pump element;Ty bơm cao áp;Ty bơm cao áp;36; 15.07 ;542.52;1.1; 407,266.75 ; 480,000 ; 528,000 ;co san ;;
TLT-PO-01-0221;H105015393KMH;H105015393;9432610051;H105015393;DLLA154S284N393;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;36; 15.97 ;574.92;1.1; 431,589.25 ; 540,000 ; 594,000 ;T5;;
TLT-PO-01-0221;H105015413KMH;H105015413;9432610018;H105015413;DLLA154S324N413;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;36; 13.06 ;470.16;1.1; 352,946.50 ; 400,000 ; 440,000 ;T5;;
TLT-PO-01-0221;H105015419KMH;H105015419;9432610024;H105015419;DLLA154S334N419;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;36; 13.44 ;483.84;1.1; 363,216.00 ; 460,000 ; 506,000 ;co san ;;
TLT-PO-01-0221;H105017010KMH;H105017010;9432610078;H105017010;DLLA160PN010;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;36; 16.67 ;600.12;1.1; 450,506.75 ; 530,000 ; 583,000 ;T5;;
TLT-PO-01-0221;94436100743YL;9443610074;9443610074;131152-2220;A148;3YL;pump element;Ty bơm cao áp;Ty bơm cao áp;36; 14.88 ;535.68;1.1; 402,132.00 ; 470,000 ; 517,000 ;T5;;
TLT-PO-01-0221;94136141943YL;9413614194;9413614194;131154-5620;A298;3YL;pump element;Ty bơm cao áp;Ty bơm cao áp;24; 14.24 ;341.76;1.1; 384,836.00 ; 450,000 ; 495,000 ;co san ;;
TLT-PO-01-0221;94436102183YL;9443610218;9443610218;131151-7320;A89;3YL;pump element;Ty bơm cao áp;Ty bơm cao áp;24; 13.66 ;327.84;1.1; 369,161.50 ; 430,000 ; 473,000 ;co san ;;
TLT-PO-01-0221;94436104683YL;9443610468;9443610468;131154-2220;A264;3YL;pump element;Ty bơm cao áp;Ty bơm cao áp;24; 15.10 ;362.4;1.1; 408,077.50 ; 480,000 ; 528,000 ;T5;;
TLT-PO-01-0221;94436107913YL;9443610791;9443610791;131154-1120;A253;3YL;pump element;Ty bơm cao áp;Ty bơm cao áp;24; 16.03 ;384.72;1.1; 433,210.75 ; 510,000 ; 561,000 ;co san ;;
TLT-PO-01-0221;H105015869KMH;H105015869;9432610266;H105015869;DLLA158SN869;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;24; 16.67 ;400.08;1.1; 450,506.75 ; 570,000 ; 627,000 ;T5;;
TLT-PO-01-0221;H105017005KMH;H105017005;9432610161;H105017005;DLLA154PN005;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;24; 18.21 ;437.04;1.1; 492,125.25 ; 580,000 ; 638,000 ;T5;;
TLT-PO-01-0221;H105017009KMH;H105017009;9432610175;H105017009;DLLA152PN009;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;24; 16.93 ;406.32;1.1; 457,533.25 ; 540,000 ; 594,000 ;T5;;
TLT-PO-01-0221;H105025029KMH;H105025029;9432610450;H105025029;DLLA153SM029;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;24; 17.73 ;425.52;1.1; 479,153.25 ; 620,000 ; 682,000 ;co san ;;
TLT-PO-01-0221;H105025145KMH;H105025145;9432610870;H105025145;DLLA151SM145;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;24; 21.12 ;506.88;1.1; 570,768.00 ; 670,000 ; 737,000 ;T5;;
TLT-PO-01-0221;H105025304KMH;H105025304;9432610764;H105025304;DLLA149SM304;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;24; 15.39 ;369.36;1.1; 415,914.75 ; 500,000 ; 550,000 ;T5;;
TLT-PO-01-0221;043317145475Y;0433171454;0433171454;;DLLA145P606;75Y;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 12.45 ;149.4;1.1; 336,461.25 ; 500,000 ; 550,000 ;T4;;
TLT-PO-01-0221;94136101353YL;9413610135;9413610135;131152-6820;A204;3YL;pump element;Ty bơm cao áp;Ty bơm cao áp;12; 14.82 ;177.84;1.1; 400,510.50 ; 470,000 ; 517,000 ;T5;;
TLT-PO-01-0221;94436103733YL;9443610373;9443610373;131154-3920;A281;3YL;pump element;Ty bơm cao áp;Ty bơm cao áp;12; 13.47 ;161.64;1.1; 364,026.75 ; 500,000 ; 550,000 ;co san ;;
TLT-PO-01-0221;H105015569KMH;H105015569;9432610899;H105015569;DLLA142SN569;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 13.74 ;164.88;1.1; 371,323.50 ; 630,000 ; 693,000 ;T5;;
TLT-PO-01-0221;H105015783KMH;H105015783;9432611270;H105015783;DLLA149SN783;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 15.18 ;182.16;1.1; 410,239.50 ; 690,000 ; 759,000 ;T5;;
TLT-PO-01-0221;H105015852KMH;H105015852;9432610305;H105015852;DLLA158SN852;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 15.78 ;189.36;1.1; 426,454.50 ; 500,000 ; 550,000 ;T5;;
TLT-PO-01-0221;H105017053KMH;H105017053;9432610853;H105017053;DLLA155PN053;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 15.39 ;184.68;1.1; 415,914.75 ; 740,000 ; 814,000 ;T5;;
TLT-PO-01-0221;H105017063KMH;H105017063;9432610362;H105017063;DLLA152PN063;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 18.56 ;222.72;1.1; 501,584.00 ; 640,000 ; 704,000 ;T5;;
TLT-PO-01-0221;H105017267KMH;H105017267;9432610464;H105017267;DLLA152PN267;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 17.02 ;204.24;1.1; 459,965.50 ; 540,000 ; 594,000 ;T5;;
TLT-PO-01-0221;H105017354KMH;H105017354;9432612952;H105017354;DLLA140P643;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 9.86 ;118.32;1.1; 266,466.50 ; 310,000 ; 341,000 ;T5;;
TLT-PO-01-0221;H105025012KMH;H105025012;9432610821;H105025012;DLLA145SM012;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 19.14 ;229.68;1.1; 517,258.50 ; 610,000 ; 671,000 ;T5;;
TLT-PO-01-0221;H105025303KMH;H105025303;9432610769;H105025303;DLLA150SM303;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 18.78 ;225.36;1.1; 507,529.50 ; 600,000 ; 660,000 ;co san ;;
TLT-PO-01-0221;H105025325KMH;H105025325;9432611628;H105025325;DLLA151SM325;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 15.23 ;182.76;1.1; 411,590.75 ; 490,000 ; 539,000 ;T5;;
TLT-PO-01-0221;H105025327KMH;H105025327;9432610772;H105025327;DLLA147SM327;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 18.98 ;227.76;1.1; 512,934.50 ; 640,000 ; 704,000 ;T5;;
TTL-PO-02-0221;04331754148GA;0433175414;0433175414;;DSLA146P1409;8GA;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;300; 23.24 ;6972;1.1; 628,061.00 ; 780,000 ; 858,000 ;co san ;;
TTL-PO-02-0221;H105025343KMH;H105025343;9432612653;H105025343;DLLA150SM343;KMH;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;300; 15.40 ;4620;1.1; 416,185.00 ; 540,000 ; 594,000 ;co san ;;
TTL-PO-02-0221;04331754138GA;0433175413;0433175413;;DSLA146P1398;8GA;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;120; 23.24 ;2788.8;1.1; 628,061.00 ; 780,000 ; 858,000 ;co san ;;
TTL-PO-02-0221;F002C4003041N;F002C40030;F002C40030;;DLLA160P2256;41N;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;120; 7.46 ;895.2;1.1; 201,606.50 ; 340,000 ; 374,000 ;co san ;;
TTL-PO-02-0221;F002C4003141N;F002C40031;F002C40031;;DLLA156P2255;41N;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;120; 7.81 ;937.2;1.1; 211,065.25 ; 360,000 ; 396,000 ;co san ;;
TTL-PO-02-0221;04331718068GA;0433171806;0433171806;;DLLA142P1283;8GA;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;90; 9.22 ;829.8;1.1; 249,170.50 ; 350,000 ; 385,000 ;T7;;
TTL-PO-02-0221;0440050007810;0440050007;0440050007;;;810;Fuel pump;;Bơm cấp dầu Maxxforce;40; 60.00 ;2400;1.1; 1,621,500.00 ; 2,800,000 ; 3,080,000 ;T6;;
TTL-PO-02-0221;04331754848GA;0433175484;0433175484;;DSLA150P1729;8GA;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;36; 11.42 ;411.12;1.1; 308,625.50 ; 390,000 ; 429,000 ;T4;;
TTL-PO-02-0221;2434614020770;2434614020;2434614020;;;770;Spring;;Loxo / béc D60;30; 0.32 ;9.6;1.1; 8,648.00 ; 10,000 ; 11,000 ;T8;;
TTL-PO-02-0221;F00H4S0008741;F00H4S0008;F00H4S0008;;;741;Repair kit;Bộ phận của đầu kim phun cao áp;Loxo +núm / béc D60;30; 7.33 ;219.9;1.1; 198,093.25 ; 230,000 ; 253,000 ;T4;;
TTL-PO-02-0221;F00ZB20001741;F00ZB20001;F00ZB20001;;;741;Pressure spindle;;Núm / béc D60;30; 0.74 ;22.2;1.1; 19,998.50 ; 20,000 ; 22,000 ;T4;;
TTL-PO-02-0221;043317208075N;0433172080;0433172080;;DLLA155P1771;75N;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;24; 32.00 ;768;1.1; 864,800.00 ; 1,080,000 ; 1,188,000 ;T5;;
TTL-PO-02-0221;04331722218GA;0433172221;0433172221;;DLLA148P2221;8GA;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;24; 18.05 ;433.2;1.1; 487,801.25 ; 610,000 ; 671,000 ;T7;;
TTL-PO-02-0221;0281006117000;0281006117;0281006117;;;000;Pressure sensor;Cảm biến áp suất dầu;Cảm biến áp suất dầu ống Raill Maxxforce;20; 21.00 ;420;1.1; 567,525.00 ; 1,000,000 ; 1,100,000 ;T5;;
TTL-PO-02-0221;F00N210223391;F00N210223;F00N210223;;;391;Metering unit;Van điều tiết dầu bơm cao áp;Van điều tiết dầu / DD15;20; 67.26 ;1345.2;1.1; 1,817,701.50 ; 3,100,000 ; 3,410,000 ;T5;;
TTL-PO-02-0221;04331718438GA;0433171843;0433171843;;DLLA118P1357;8GA;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 28.50 ;342;1.1; 770,212.50 ; 960,000 ; 1,056,000 ;T7;;
TTL-PO-02-0221;043317187175N;0433171871;0433171871;;DLLA146P1405;75N;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 27.62 ;331.44;1.1; 746,430.50 ; 935,000 ; 1,028,500 ;T5;;
TTL-PO-02-0221;04331718758GA;0433171875;0433171875;;DLLA144P1413;8GA;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 9.22 ;110.64;1.1; 249,170.50 ; 350,000 ; 385,000 ;T7;;
TTL-PO-02-0221;04331719824N6;0433171982;0433171982;;DLLA156P1608;4N6;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 27.50 ;330;1.1; 743,187.50 ; 920,000 ; 1,012,000 ;T4;;
TTL-PO-02-0221;043317198475N;0433171984;0433171984;;DLLA146P1610;75N;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;12; 30.72 ;368.64;1.1; 830,208.00 ; 1,050,000 ; 1,155,000 ;T5;;
TTL-PO-02-0221;F002B7004441N;F002B70044;F002B70044;;;41N;Delivery Valve Holder;Van phân phối điều khiển dầu;Van phân phối dầu;12; 2.50 ;30;1.1; 67,562.50 ; 90,000 ; 99,000 ;T4;;
TTL-PO-02-0221;F00RJ01727879;F00RJ01727;F00RJ01727;;;879;Valve Set;Van điều khiển dầu bơm cao áp;Van béc;12; 23.74 ;284.88;1.1; 641,573.50 ; 870,000 ; 957,000 ;T6;;
TTL-PO-02-0221;F00RJ02213751;F00RJ02213;F00RJ02213;;;751;Valve Set;Van điều khiển dầu bơm cao áp;Van béc;12; 39.00 ;468;1.1; 1,053,975.00 ; 1,320,000 ; 1,452,000 ;T5;;
TTL-PO-02-0221;F00VC01352770;F00VC01352;F00VC01352;;;770;Valve Set;Van điều khiển dầu bơm cao áp;Van béc;12; 27.00 ;324;1.1; 729,675.00 ; 1,100,000 ; 1,210,000 ;T4;;
TTL-PO-02-0221;F018B06804741;F018B06804;F018B06804;;;741;Adaptor plate;Bộ phận kim phun cao áp;Đĩa đệm kim phun S60;12; 8.93 ;107.16;1.1; 241,333.25 ; 300,000 ; 330,000 ;T4;;
TTL-PO-02-0221;0281002942001;0281002942;0281002942;;;001;Pressure sensor;Cảm biến áp suất dầu;Cảm biến áp suất dầu ống Rail DD15;10; 22.11 ;221.1;1.1; 597,522.75 ; 800,000 ; 880,000 ;T4;;
TTL-PO-02-0221;F002H23520772;F002H23520;F002H23520;;;772;Hand feed pump;Tay cầm máy bơm phun cao áp;Cần bơm tay trên bơm cao áp;10; 3.36 ;33.6;1.1; 90,804.00 ; 110,000 ; 121,000 ;T7;;
TTL-PO-02-0221;F00N010001390;F00N010001;F00N010001;;;390;Pressure limiting valve;Van giới hạn áp suất dầu;Van giới hạn áp suất dầu trên ống Rail xe Maxxforce;10; 16.16 ;161.6;1.1; 436,724.00 ; 1,000,000 ; 1,100,000 ;T4;;
TTL-PO-02-0221;04331720408GA;0433172040;0433172040;;DLLA118P1697;8GA;Hole-Type Nozzle;Đầu kim phun cao áp;Đầu kim phun cao áp;6; 28.38 ;170.28;1.1; 766,969.50 ; 960,000 ; 1,056,000 ;T4;;
TTL-PO-02-0221;0445120265879;0445120265;0445120265;;;879;Injector Assy;Béc nguyên cây;Béc nguyên cây;6; 100.00 ;600;1.1; 2,702,500.00 ; 3,550,000 ; 3,905,000 ;T7;;
TTL-PO-02-0221;F00RJ01941751;F00RJ01941;F00RJ01941;;;751;Valve set;Van điều khiển dầu bơm cao áp;Van béc;6; 27.00 ;162;1.1; 729,675.00 ; 1,000,000 ; 1,100,000 ;T5;;
TTL-PO-02-0221;F00RJ02035879;F00RJ02035;F00RJ02035;;;879;Valve Set                                                          ;Van điều khiển dầu bơm cao áp;Van béc;6; 21.50 ;129;1.1; 581,037.50 ; 790,000 ; 869,000 ;T7;;
TTL-PO-02-0221;F00RJ02130751;F00RJ02130;F00RJ02130;;;751;Valve Set;Van điều khiển dầu bơm cao áp;Van béc;6; 28.67 ;172.02;1.1; 774,806.75 ; 1,050,000 ; 1,155,000 ;T5;;
TTL-PO-02-0221;F00VC01033770;F00VC01033;F00VC01033;;;770;Valve set;Van điều khiển dầu bơm cao áp;Van béc;6; 25.49 ;152.94;1.1; 688,867.25 ; 940,000 ; 1,034,000 ;co san ;;
TTL-PO-02-0221;F00N210061000;F00N210061;F00N210061;;;000;Metering unit;Van điều tiết dầu bơm cao áp;Van điều tiết dầu;5; 29.86 ;149.3;1.1; 806,966.50 ; 1,800,000 ; 1,980,000 ;T6;;
"""


def run():
    # file1 = open('data.txt', 'r', encoding="utf8")
    lines = data.splitlines()
    for line in lines[:5]:
        line = line.split(";")
        po = POModel()
        po.po_no = line[0]
        po.pn_13 = line[1]
        po.pn_10 = line[2]
        po.bosch_no = line[3]
        po.z_exel_no = line[4]
        po.stamping = line[5]
        po.country = line[6]
        po.english_des = line[7]
        po.import_des = line[8]
        po.app_des = line[9]
        po.quantity = line[10]
        po.dap_price = line[11]
        po.extension_price = line[12]
        po.tax = line[13]
        po.gia_von = line[14]
        po.gia_si = line[15]
        po.gia_le = line[16]
        po.lead_time = line[17]
        po.customer = line[18]
        po.remarks = line[19]

