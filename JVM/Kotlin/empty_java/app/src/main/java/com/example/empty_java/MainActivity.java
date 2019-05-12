package com.example.empty_java;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        Button btn1 = findViewById(R.id.button1);

        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Toast tot = Toast.makeText(MainActivity.this, "我爱我的莲儿", Toast.LENGTH_LONG);
                tot.show();

            }
        });


    }
}
