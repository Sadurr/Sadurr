package com.example.toDoApplication.repo;

import com.example.toDoApplication.model.ToDoItem;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ToDoRepo extends JpaRepository<ToDoItem, Long> {
}
