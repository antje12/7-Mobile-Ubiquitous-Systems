package com.example.mobile_sensing

import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.util.Log

class AccelerometerListener : SensorEventListener {

    private var lastUpdate: Long = 0
    private var last_x: Float = 0f
    private  var last_y: Float = 0f
    private  var last_z: Float = 0f

    override fun onSensorChanged(event: SensorEvent) {
        val mySensor: Sensor = event.sensor

        if (mySensor.type == Sensor.TYPE_ACCELEROMETER) {
            val x: Float = event.values.get(0)
            val y: Float = event.values.get(1)
            val z: Float = event.values.get(2)

            val curTime = System.currentTimeMillis()
            if (curTime - lastUpdate > 100) {
                lastUpdate = curTime
                last_x = x
                last_y = y
                last_z = z

                Log.i("ACCELEROMETER", "XYZ = "
                        + "%.2f".format(x) + " | "
                        + "%.2f".format(y) + " | "
                        + "%.2f".format(z))
            }
        }
    }

    override fun onAccuracyChanged(p0: Sensor?, p1: Int) {

    }
}