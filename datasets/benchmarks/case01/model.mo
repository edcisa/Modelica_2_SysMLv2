model SimpleResistor
  parameter Real R = 100;
  Voltage v;
  Current i;
equation
  v = R * i;
end SimpleResistor;
